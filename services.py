from dataclasses import dataclass
from token_refresh import TokenRefresh
from data.dataid import spreadsheet_id
import requests

@dataclass
class Services:

  conta:str
  acess_token:str
  refresh_token:str

  def __init__(self):
      
    token_refresh = TokenRefresh(spreadsheet_id)
    tokens = token_refresh.token

    self.conta = tokens['conta']
    self.acess_token = tokens['access_token']
    self.refresh_token = tokens['refresh_token']

    print(f"Conta {self.conta}, Acess Token {self.acess_token}, Refresh Token {self.refresh_token}")



  def infouser(self):
    url = "https://api.mercadolibre.com/users/me"

    payload = {}
    headers = {
      'Authorization': f'Bearer {self.acess_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    id_user = data.get('id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    address = data.get('address', {}).get('address')  
    state = data.get('address', {}).get('state')

    return {"id" : id_user, "name" : first_name, "last_name" : last_name, "email": email, "address": address, "state": state}
  
