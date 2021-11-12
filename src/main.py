import pandas as pd
import glob

file_extension = '.csv'
all_filenames = [i for i in glob.glob(f"../dataset/Song-Lyrics-Dataset/csv/*{file_extension}")]

combinedLyrics = pd.concat([pd.read_csv(f) for f in all_filenames])

combinedLyrics = combinedLyrics.drop('Unnamed: 0', 1)

combinedLyrics.to_csv('../dataset/Song-Lyrics-Dataset/csv/combined.csv', index=False)

musicGenres = pd.read_csv('../dataset/Music-Genres/csv/songs.csv', sep=';')

musicGenres.columns = [
    "ID", 
    "Title", 
    "Artist", 
    "Position", 
    "Genre"
]

combinedLyrics = combinedLyrics.drop(["Year"], axis=1)
musicGenres = musicGenres.drop(["ID", "Position"], axis=1)

merged = pd.merge(combinedLyrics, musicGenres, on=['Artist', 'Title'])

merged.drop_duplicates(keep = 'first', inplace = True)

merged.groupby(['Artist', 'Title', 'Album', 'Date', 'Lyric']).sum()

merged.to_csv('../dataset/merged.csv', index=False)

