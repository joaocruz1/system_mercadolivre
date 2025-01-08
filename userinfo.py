import requests

url = "https://api.mercadolibre.com/users/me"

payload = {}
headers = {
  'Authorization': 'Bearer APP_USR-8559585531006747-010719-9fc517db1a04080b4f7b4725cb7ed4f4-1289575784'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
