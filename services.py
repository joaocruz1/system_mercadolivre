from dataclasses import dataclass
from token_refresh import TokenRefresh
from database import Shop
import mimetypes
import requests
import json


@dataclass
class Services:

  conta:str
  access_token:str
  refresh_token:str
  api_url: str = "https://api.mercadolibre.com"
  id_user:str = None
  orders: list = None

  def __init__(self):
      
    token_refresh = TokenRefresh()
    tokens =  token_refresh.Auth_AccessToken()

    self.conta = tokens['conta']
    self.access_token = tokens['access_token']
    self.refresh_token = tokens['refresh_token']

    print(self.refresh_token)


  def infouser(self):
    url = f"{self.api_url}/users/me"

    payload = {}
    headers = {
      'Authorization': f'Bearer {self.access_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    self.id_user = data.get('id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    address = data.get('address', {}).get('address')  
    state = data.get('address', {}).get('state')

    return {"id" : self.id_user, "name" : first_name, "last_name" : last_name, "email": email, "address": address, "state": state}
  
  def import_id_products(self):
    
    url = f"{self.api_url}/users/{self.id_user}/items/search"

    payload = {}
    headers = {
      'Authorization': f'Bearer {self.access_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    products_id = data.get('results', [])  
    

    return products_id
  
  def import_info_products_list(self,products_id):
    
    products_info_list = []

    for product in products_id:
      url = f"{self.api_url}/items/{product}"

      payload = {}
      headers = {
        'Authorization': f'Bearer {self.access_token}'
      }

      response = requests.request("GET", url, headers=headers, data=payload)
      data = response.json()
      products_info_list.append(data)
    
    return products_info_list
  
  def import_info_product(self,product_id):
      
      url = f"{self.api_url}/items/{product_id}"

      payload = {}
      headers = {
        'Authorization': f'Bearer {self.access_token}'
      }

      response = requests.request("GET", url, headers=headers, data=payload)
      product = response.json()
    
      return product
  
  def import_description_product(self, product_id):
      url = f"{self.api_url}/items/{product_id}/description"

      payload = {}
      headers = {
        'Authorization': f'Bearer {self.access_token}'
      }

      response = requests.request("GET", url, headers=headers, data=payload)
      data = response.json()

      return data

  def edit_infos_product(self,product_id,new_product_img,product_title,product_description,product_price,product_condition,product_status,product_quantity):

    url = f"{self.api_url}/items/{product_id}"
    
    payload = {}

    if product_title is not None:
        payload["title"] = str(product_title)
    
    if product_price is not None:
        payload["price"] = float(product_price)
    
    if product_condition is not None:
        payload["condition"] = str(product_condition)
    
    if product_status is not None:
        payload["status"] = str(product_status)
    
    if product_quantity is not None:
        payload["available_quantity"] = int(product_quantity)
    
    headers = {
        'Authorization': f'Bearer {self.access_token}',
        'Content-Type': 'application/json'
    }
    
    try:
        if payload:
            response = requests.request("PUT", url, headers=headers, data=json.dumps(payload))
            if response.status_code not in [200, 201]:
                error_data = response.json()
                return {"status": "error", "message": error_data.get("message", "Erro ao atualizar o produto.")}
        
        if product_description is not None:
            description_url = f"{self.api_url}/items/{product_id}/description"
            description_payload = json.dumps({
                "plain_text": product_description
            })
            description_response = requests.request("PUT", description_url, headers=headers, data=description_payload)
            if description_response.status_code != 200:
                error_data = description_response.json()
                return {"status": "error", "message": error_data.get("message", "Erro ao atualizar a descrição.")}
        
     
        if new_product_img is not None:
        
            mime_type, _ = mimetypes.guess_type(new_product_img.filename)
            upload_url = f"{self.api_url}/pictures/items/upload"
            
            file_content = new_product_img.read()
            files = [
                ('file', (new_product_img.filename, file_content, str(mime_type)))
            ]
            
            upload_headers = {
                'Authorization': f'Bearer {self.access_token}'
            }
            
            upload_response = requests.request("POST", upload_url, headers=upload_headers, files=files)
            data = upload_response.json()

            if upload_response.status_code not in [200, 201]: 
                error_data = upload_response.json()
                return {"status": "error", "message": error_data.get("message", "Erro ao fazer upload da imagem.")}

            associate_url = f"{self.api_url}/items/{product_id}/pictures"
            associate_payload = json.dumps({
                "id": data.get("id")
            })
            associate_headers = {
                'Authorization': f'Bearer {self.access_token}',
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            
            associate_response = requests.request("POST", associate_url, headers=associate_headers, data=associate_payload)

            if associate_response.status_code not in [200,201]: 
                error_data = associate_response.json()
                return {"status": "error", "message": error_data.get("message", "Erro ao associar a imagem ao produto.")}

        return {"status": "success", "message": "Produto atualizado com sucesso."}
    
    except Exception as e:  
        return {"status": "error", "message": f"Erro ao processar a requisição: {str(e)}"}

  def delete_image_product(self,product_id, img_id):

      url = f"{self.api_url}/items/{product_id}/pictures/{img_id}?access_token={self.access_token}"

      payload = {}
      headers = {}

      try:
        response = requests.request("DELETE", url, headers=headers, data=payload)
        if response.status_code == 200:
            return {"status": "success", "message": "Imagem deletada com sucesso."}
        else:
            error_data = response.json()
            return {"status": "error", "message": error_data.get("message", "Erro ao deletar a imagem.")}
      except Exception as e:
        return {"status": "error", "message": f"Erro ao processar a requisição: {str(e)}"}
    
  def import_orders(self):
    
    url = f"{self.api_url}/orders/search?seller={self.id_user}&tags=mshops"

    payload = {}
    headers = {
      'Authorization': f'Bearer {self.access_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    orders = data.get('results', [])
    orders_amount = len(orders)
    orders_id = []

    for order in orders:

      orders_id.append(order.get('id'))

    return orders_amount

  def import_feedbacks(self,orders_id):
    pass

  def import_categories(self):

    url = f"{self.api_url}/sites/MLB/categories/all"

    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    categories = []

    for category in data.values():

      id = category.get('id',[])
      name = category.get('name',[])
      subcategories = category.get('children_categories',[])
      subcategories_list = []

      for sub in subcategories:
        id = sub.get('id',[])
        name = sub.get('name',[])
        subcategories_list.append({ 'id': id, 'name': name})

      categories.append(
        {  'id': id,
           'name' : name,
           'subcategories' : subcategories_list
        }
      )
    return categories

  def import_category_attributes(self,category_id):

    url = f"{self.api_url}/categories/{category_id}/attributes"

    payload = {}
    headers = {
      'Authorization': f'Bearer {self.access_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()
    
  def publi_product(self,title,category_id,price,avaible_quantity,condition,description, attributes):


    url = f"{self.api_url}/items"

    payload = json.dumps({
      "title": f"{title}",
      "category_id": f"{category_id}",
      "price": price,
      "currency_id": "BRL",
      "available_quantity": avaible_quantity,
      "buying_mode": "buy_it_now",
      "listing_type_id": "gold_special",
      "condition": f"{condition}",
      "description": f"{description}",
      "pictures": [
        {
          "source": "URL_DA_IMAGEM_1"
        },
        {
          "source": "URL_DA_IMAGEM_2"
        }
      ],
      "shipping": {
        "mode": "me2",
        "free_shipping": True
      },
      "attributes": attributes
    })
    headers = {
      'Authorization': f'Bearer {self.access_token}',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


    

      





    
