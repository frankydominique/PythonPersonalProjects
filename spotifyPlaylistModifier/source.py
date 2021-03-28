import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 
client_secret = 

client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                      client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

name = "Daniel Caesar"

result = sp.search(name)

artist_uri = result['tracks']['items'][0]['artists'][0]['uri']

sp_albums = sp.artist_albums(artist_uri, album_type='album')

album_names=[]
album_uris=[]
for i in range(len(sp_albums['items'])):
    album_names.append(sp_albums['items'][i]['name'])
    album_uris.append(sp_albums['items'][i]['uri'])

album_names
album_uris




        
