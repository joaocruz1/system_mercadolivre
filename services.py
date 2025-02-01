from dataclasses import dataclass
from token_refresh import TokenRefresh
from data.dataid import spreadsheet_id
from database import Shop
import requests

@dataclass
class Services:

  conta:str
  access_token:str
  refresh_token:str
  id_user:str = None
  products: list = None
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
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    address = data.get('address', {}).get('address')  
    state = data.get('address', {}).get('state')

    return {"id" : self.id_user, "name" : first_name, "last_name" : last_name, "email": email, "address": address, "state": state}
  
  def search_products(self):
    
    url = f"https://api.mercadolibre.com/users/{self.id_user}/items/search"

    payload = {}
    headers = {
      'Authorization': f'Bearer {self.access_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    self.products = data.get('results', [])  

    return len(self.products)
  
  def import_orders(self):

    url = f"https://api.mercadolibre.com/orders/search?seller={self.id_user}&tags=mshops"

    payload = {}
    headers = {
      'Authorization': f'Bearer {self.access_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response.json()
    orders = response.get('results', [])
    products_quantity = len(orders)
    orders_id = []

    for order in orders:

      orders_id.append(order.get('id'))

    return products_quantity, orders_id




  def import_feedbacks(self,orders_id):
    pass

      





    
