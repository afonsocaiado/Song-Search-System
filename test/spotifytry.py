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

column_names = ['title','artist','album','popularity']
data = pd.DataFrame(columns=column_names)

results = sp.playlist_tracks(playlist_URI)

n = 0

while results['next']:

    for track in results['items']:
        #URI
        track_uri = track["track"]["uri"]
        
        #Track name
        track_name = track["track"]["name"]
        # track_genre = track["track"]["genres"]
        # track_date = track["track"]["date"]
        
        #Main Artist
        artist_uri = track["track"]["artists"][0]["uri"]
        artist_info = sp.artist(artist_uri)
        
        #Name, popularity, genre
        artist_name = track["track"]["artists"][0]["name"]
        artist_pop = artist_info["popularity"]
        artist_genres = artist_info["genres"]
        # print(artist_genres)
        
        #Album
        album = track["track"]["album"]["name"]
        
        #Popularity of the track
        track_pop = track["track"]["popularity"]

        data.iloc[n]=[track_name,artist_name,album,track_pop]

    results = sp.next(results)

data.to_csv("spotifytest.csv", index=False)
