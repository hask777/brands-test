import requests

ngrok_url = 'https://5b4fa48a9c17.ngrok.io'
endpoint = f'{ngrok_url}/brands'

r =requests.post(endpoint, json={})
print(r.json()['data'])