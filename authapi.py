from dataclasses import dataclass

@dataclass 

class AuthApi:
    client_id:int
    secret_key:str
    acess_token:str
    refresh_token:str