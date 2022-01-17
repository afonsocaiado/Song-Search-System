import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 

cid = '8ff48ed1961349108ea38a026509e0b5'
secret = 'f1594e8013a745868352212103f013fa'

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_link = "https://open.spotify.com/playlist/0jDWpd5lTinKFpdTVKHnWk?si=b9d988f28cf74505limit=200"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

column_names = ['Title','Artist','Top Genre','Duration','Popularity','BPM','Danceability','Energy','Valence']
data = pd.DataFrame(columns=column_names)

results = sp.playlist_tracks(playlist_URI)

n = 1

while results['next']:

    for track in results['items']:

        print(n)

        #URI
        track_uri = track["track"]["uri"]

        #Track's main artist
        artist_uri = track["track"]["artists"][0]["uri"]
        artist_info = sp.artist(artist_uri)
        
        artist_name = track["track"]["artists"][0]["name"]
        artist_pop = artist_info["popularity"]
        artist_genres = artist_info["genres"]

        if len(artist_genres) > 1:
            artist_top_genre = artist_info["genres"][0]
        else:
            artist_top_genre = ""
        
        #Track name
        track_name = track["track"]["name"]

        word = "(feat."

        if word in track_name:
            index = track_name.find(word)
            track_name = track_name[:index-1]

        #Track duration
        track_duration_ms = track["track"]["duration_ms"]
        track_duration_s = track_duration_ms * 0.001

        #Track explicit
        track_explicit = track["track"]["explicit"]
        
        #Popularity of the track
        track_pop = track["track"]["popularity"]

        #Track audio features, bpm, energy, etc
        track_audio_features = sp.audio_features(track_uri)[0]

        track_bpm = track_audio_features["tempo"]
        track_danceability = track_audio_features["danceability"]
        track_energy = track_audio_features["energy"]
        track_valence = track_audio_features["valence"]

        info = {'Artist': artist_name, 'Title': track_name, 'Top Genre': artist_top_genre, 'Duration': track_duration_s, 'Popularity': track_pop, 'BPM': track_bpm, 'Danceability': track_danceability, 'Energy': track_energy, 'Valence': track_valence}

        data = data.append(info, ignore_index=True)

        n += 1

    results = sp.next(results)

data.to_csv("spotifyData.csv", index=False)
