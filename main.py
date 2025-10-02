from auth.token_handler import *
from extract.fetch_data import *


token = get_token()
artist_id = get_artist_id(token, "acdc")
artist_albums = get_artist_albums(token, artist_id)

for album in artist_albums:
    print(album["name"])