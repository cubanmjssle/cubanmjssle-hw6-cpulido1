import requests
import base64
from secrets import *



client_creds = f"{client_id}:{client_secret}"
type(client_creds)
#client_creds.encode().decode()

client_creds_b64 = base64.b64encode(client_creds.encode())
#print(client_creds_b64)

#base64.b64decode(client_creds_b64)

token_url = "https://accounts.spotify.com/api/token"
method = "POST"
token_data = {
        "grant_type" : "client_credentials"
}
token_headers = {

    "Authorization" : f"Basic {client_creds_b64.decode()}"
}

r = requests.post(token_url, data = token_data, headers = token_headers)
response = r.json()

for i in range(10):
    print(response['albums']['items'][i]['name'])

    accessToken = r.json['access_token']

