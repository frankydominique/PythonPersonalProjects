import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = ''
client_secret = ''

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
    print('adding ' + track['name'])
    track_uris.append(track['uri'])
    print('uri: ' + track['uri'])
    track_ids.append(track['id'])
    print('id: ' + track['id'])

spotifyTrackFeatures = []
for track in track_ids:
    spotifyTrackFeatures.append(spotify.audio_features(track))

songsWFeatures = {}
for i in range(10):
    trackFeatures = {}
    trackFeatures['danceability'] = spotifyTrackFeatures[i][0]['danceability']
    trackFeatures['energy'] = spotifyTrackFeatures[i][0]['energy']
    trackFeatures['loudness'] = spotifyTrackFeatures[i][0]['loudness']
    trackFeatures['acousticness'] = spotifyTrackFeatures[i][0]['acousticness']
    trackFeatures['instrumentalness'] = spotifyTrackFeatures[i][0]['instrumentalness']
    trackFeatures['speechiness'] = spotifyTrackFeatures[i][0]['speechiness']
    trackFeatures['valence'] = spotifyTrackFeatures[i][0]['valence']
    songsWFeatures[track_names[i]] = trackFeatures

print(songsWFeatures)
    
    
    
    






