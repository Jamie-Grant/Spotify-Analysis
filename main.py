#Token Auth

from dotenv import load_dotenv
import base64
import os
import json
from requests import post, get

load_dotenv()

# Load client_id and client_secret from .env file 

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Spotify needs an auth string to gain access to a token. The auth string needs to include
# both client id and secret encoded with base64. 

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials"
    }

    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_artist_id(token, artist_name):
    headers = get_auth_header(token)
    url = "https://api.spotify.com/v1/search"
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url + query

    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    return json_result["artists"]["items"][0]["id"]

token = get_token()

print(get_artist_id(token, "acdc"))