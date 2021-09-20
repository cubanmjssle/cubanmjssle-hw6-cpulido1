import requests
import base64
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

#Spotify database
AUTH_URL = 'https://accounts.spotify.com/api/token'

# used to hide, ID and Secret
CLIENT_ID = os.getenv('client_id')
CLIENT_SECRET = os.getenv('client_secret')

#POST
auth_request = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# encoding a message to base64
message = f'{CLIENT_ID} : {CLIENT_SECRET}'
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')


#convert the response to JSON
auth_response_data = auth_request.json()

# save the access token
auth_token = auth_response_data['access_token']

# base URL of all Spotify API endpoints, with specific new releases and header 
BASE_URL = f"https://api.spotify.com/v1/"
new_release_URL = 'browse/new-releases'
headers = {
    "Authorization": "Bearer " + auth_token
}

# actual GET request 
r = requests.get(BASE_URL + new_release_URL, headers=headers)

#convert response to JSON
response = r.json()

for i in range(10):
    print(response['albums']['items'][i]['name'])