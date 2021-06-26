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
    #print('adding ' + track['name'])
    track_uris.append(track['uri'])
    #print('uri: ' + track['uri'])
    track_ids.append(track['id'])
    #print('id: ' + track['id'])

spotifyTrackFeatures = []
for track in track_ids:
    spotifyTrackFeatures.append(spotify.audio_features(track))

songsWFeatures = {}
for i in range(10):
    trackFeatures = {}
    trackFeatures['danceability'] = spotifyTrackFeatures[i][0]['danceability']
    trackFeatures['energy'] = spotifyTrackFeatures[i][0]['energy']
    #trackFeatures['loudness'] = spotifyTrackFeatures[i][0]['loudness']
    #trackFeatures['start loudness'] = spotify.audio_analysis(track_ids[i]).get("sections")[0].get("loudness")
    #trackFeatures['start tempo'] = spotify.audio_analysis(track_ids[i]).get("sections")[0].get("tempo")
    sectionsLen = len(spotify.audio_analysis(track_ids[i]).get("sections"))
    #trackFeatures['end loudness'] = spotify.audio_analysis(track_ids[i]).get("sections")[sectionsLen - 1].get("loudness")
    #trackFeatures['end tempo'] = spotify.audio_analysis(track_ids[i]).get("sections")[sectionsLen - 1].get("tempo")
    countBeats = 0
    countTatums = 0
    for j in range(len(spotify.audio_analysis(track_ids[i]).get("beats"))):
        countBeats = countBeats + 1
    for k in range(len(spotify.audio_analysis(track_ids[i]).get("tatums"))):
        countTatums = countTatums + 1
    songDuration = spotify.audio_analysis(track_ids[i]).get("track").get("duration") / 60
    trackFeatures['beat per minute'] = countBeats / songDuration
    trackFeatures['tatum per minute'] = countTatums / songDuration
    songsWFeatures[track_names[i]] = trackFeatures
    

print(songsWFeatures)
#print(songsWFeatures.get("Don't Wanna Cry","Failed"))
#print(spotify.audio_analysis(track_ids[0]).get("beats"))

## energy, valence, loudness, danceability
## sections (an array spotify breaks up the different parts of the song, want beginning
    ##end, and middle)
## in sections, keys that matter are loudness, tempo


# make a weighted score using beat, tatum, energy, danceability
# will i need to standardize the values? yeah ://


weightedScores = []
for song in songsWFeatures:
    songAndScore = {}
    score = songsWFeatures[song].get('beat per minute') * .75 + songsWFeatures[song].get('tatum per minute') * .126 + songsWFeatures[song].get('energy') + songsWFeatures[song].get('danceability')
    print(score)

    
    
    





