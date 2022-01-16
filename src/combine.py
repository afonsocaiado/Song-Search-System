import pandas as pd
import glob

if __name__ == '__main__':

    file_extension = '.csv'
    all_filenames = [i for i in glob.glob(f"../dataset/Song-Lyrics-Dataset/csv/*{file_extension}")]
    
    combinedLyrics = pd.concat([pd.read_csv(f) for f in all_filenames])  
    
    spotify2000 = pd.read_csv('dataset/Spotify-2000/csv/Spotify-2000.csv')
    
    decade2000 = pd.read_csv('dataset/Decades/csv/2000.csv')
    
    decade2000 = decade2000.rename(columns={'title' : 'Title', 'artist' : 'Artist', 'top genre' : 'Top Genre', 'year' : 'Year', 'bpm' : 'Beats Per Minute (BPM)', 'nrgy' : 'Energy', 'dnce' : 'Danceability', 'dB' : 'Loudness (dB)', 'live' : 'Liveness', 'val' : 'Valence', 'dur' : 'Length (Duration)', 'acous' : 'Acousticness', 'spch' : 'Speechiness', 'pop' : 'Popularity'})
    
    decade2010 = pd.read_csv('dataset/Decades/csv/2010.csv')
    
    decade2010 = decade2010.rename(columns={'title' : 'Title', 'artist' : 'Artist', 'top genre' : 'Top Genre', 'year' : 'Year', 'bpm' : 'Beats Per Minute (BPM)', 'nrgy' : 'Energy', 'dnce' : 'Danceability', 'dB' : 'Loudness (dB)', 'live' : 'Liveness', 'val' : 'Valence', 'dur' : 'Length (Duration)', 'acous' : 'Acousticness', 'spch' : 'Speechiness', 'pop' : 'Popularity'})
    
    musicGenres = pd.concat([decade2000, decade2010, spotify2000])
    
    merged = pd.merge(combinedLyrics, musicGenres, on=['Artist', 'Title'])
    
    merged.to_csv('dataset/combined.csv', index=False)
    
    print('Combined the data and wrote it to combined.csv\n')