import pandas as pd
import glob

file_extension = '.csv'
all_filenames = [i for i in glob.glob(f"../dataset/Song-Lyrics-Dataset/csv/*{file_extension}")]

combinedLyrics = pd.concat([pd.read_csv(f) for f in all_filenames])

spotify2000 = pd.read_csv('../dataset/Spotify-2000/csv/Spotify-2000.csv')

decade2000 = pd.read_csv('../dataset/Decades/csv/2000.csv')

decade2000 = decade2000.rename(columns={'title' : 'Title', 'artist' : 'Artist', 'top genre' : 'Top Genre'})

decade2010 = pd.read_csv('../dataset/Decades/csv/2010.csv')

decade2010 = decade2010.rename(columns={'title' : 'Title', 'artist' : 'Artist', 'top genre' : 'Top Genre'})

musicGenres = pd.concat([decade2000, decade2010, spotify2000])

merged = pd.merge(combinedLyrics, musicGenres, on=['Artist', 'Title'])

#import cleaning
#import extending

#merged = cleaning.clean(merged)

#merged = extending.extend(merged)

#merged.to_csv('../dataset/merged.csv', index=False)