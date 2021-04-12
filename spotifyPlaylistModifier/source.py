import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 
client_secret = 

client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                      client_secret=client_secret)

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

svt_uri = 'spotify:artist:7nqOGRxlXj7N2JYbgNEjYH'

results = spotify.artist_top_tracks(svt_uri)
track_names = []
track_uris = []
track_ids = []

for track in results['tracks'][:10]:
    track_names.append(track['name'])
    track_uris.append(track['uri'])
    track_ids.append(track['id'])

for track in track_ids:
    print(spotify.audio_analysis(track))






