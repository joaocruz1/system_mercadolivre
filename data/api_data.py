from token_refresh import TokenRefresh
from data.dataid import spreadsheet_id
from dataclasses import dataclass


@dataclass

class APIData: 
    
    conta: str = None
    acess_token: str = None
    refresh_token: str = None


    def datarows(self):
       
       token_refresh = TokenRefresh(spreadsheet_id)
       self.token = token_refresh.token

       conta = self.token['conta']
       acess_token = self.token['access_token']
       refresh_token = self.token['refresh_token']
       print(f"Conta {conta}, Acess Token {acess_token}, Refresh Token {refresh_token}")

       return conta, acess_token, refresh_token
       
