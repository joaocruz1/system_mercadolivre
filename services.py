from dataclasses import dataclass
from token_refresh import TokenRefresh
from data.dataid import spreadsheet_id
from database import Shop
import requests
import json

@dataclass
class Services:

  conta:str
  access_token:str
  refresh_token:str
  id_user:str = None
  orders: list = None

  def __init__(self):
      
    token_refresh = TokenRefresh(spreadsheet_id)
    tokens = token_refresh.token

    self.conta = tokens['conta']
    self.access_token = tokens['access_token']
    self.refresh_token = tokens['refresh_token']

    print(f"Conta {self.conta}, Acess Token {self.access_token}, Refresh Token {self.refresh_token}")

  def infouser(self):
    url = "https://api.mercadolibre.com/users/me"

    payload = {}
    headers = {
      'Authorization': f'Bearer {self.access_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    self.id_user = data.get('id')
    print(self.id_user)
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    address = data.get('address', {}).get('address')  
    state = data.get('address', {}).get('state')

    return {"id" : self.id_user, "name" : first_name, "last_name" : last_name, "email": email, "address": address, "state": state}
  
  def import_id_products(self):
    
    url = f"https://api.mercadolibre.com/users/{self.id_user}/items/search"

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
      url = f"https://api.mercadolibre.com/items/{product}"

      payload = {}
      headers = {
        'Authorization': f'Bearer {self.access_token}'
      }

      response = requests.request("GET", url, headers=headers, data=payload)
      data = response.json()
      products_info_list.append(data)
    
    return products_info_list
  
  def import_info_product(self,product_id):
      
      url = f"https://api.mercadolibre.com/items/{product_id}"

      payload = {}
      headers = {
        'Authorization': f'Bearer {self.access_token}'
      }

      response = requests.request("GET", url, headers=headers, data=payload)
      product = response.json()
    
      return product

  
  def import_orders(self):

    url = f"https://api.mercadolibre.com/orders/search?seller={self.id_user}&tags=mshops"

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

    url = "https://api.mercadolibre.com/sites/MLB/categories/all"

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

    
  def publi_product(self,title,category_id,price,avaible_quantity,listing_type_id,condition,description,pictures):

    url = "https://api.mercadolibre.com/items"

    payload = json.dumps({
      "title": "Mochila cinza",
      "category_id": "MLB277590",
      "price": 1500,
      "currency_id": "BRL",
      "available_quantity": 5,
      "buying_mode": "buy_it_now",
      "listing_type_id": "gold_special",
      "condition": "new",
      "description": "mochilaboa.",
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
      "attributes": [
        {
          "id": "BRAND",
          "value_name": "Marca Exemplo"
        },
        {
          "id": "PART_NUMBER",
          "value_name": "123456"
        }
      ]
    })
    headers = {
      'Authorization': f'Bearer {self.access_token}',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


    

      





    
