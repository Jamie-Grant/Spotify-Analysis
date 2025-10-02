from auth.token_handler import *

def get_artist_id(token, artist_name):
    headers = get_auth_header(token)
    url = "https://api.spotify.com/v1/search"
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url + query

    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    return json_result["artists"]["items"][0]["id"]

def get_artist_albums(token, artist_id):
    headers = get_auth_header(token)
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"

    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    
    return json_result["items"]