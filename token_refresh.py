import requests
from dataclasses import dataclass
from database import Shop


@dataclass
class TokenRefresh:


    refresh_token: str = Shop.get(Shop.id == 1).refresh_token


    def Auth_AccessToken (self):
        url = "https://api.mercadolibre.com/oauth/token"

        payload = f'grant_type=refresh_token&client_id=8559585531006747&client_secret=nirumUxTg4imSRcWxy2OrHgp7QfDNgmr&refresh_token={self.refresh_token}'
        headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        

        Shop.update(refresh_token=response.json().get('refresh_token')).where(Shop.id == 1).execute()

        return {
            "access_token": response.json().get('access_token'),
            "refresh_token": response.json().get('refresh_token'),
            "conta": response.json().get('conta')
        }

