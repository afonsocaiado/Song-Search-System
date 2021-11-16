import pandas as pd
import glob

file_extension = '.csv'
all_filenames = [i for i in glob.glob(f"../dataset/Song-Lyrics-Dataset/csv/*{file_extension}")]

combinedLyrics = pd.concat([pd.read_csv(f) for f in all_filenames])

combinedLyrics = combinedLyrics.drop(["Year", 'Unnamed: 0'], axis=1)

combinedLyrics.to_csv('../dataset/Song-Lyrics-Dataset/csv/combined.csv', index=False)

spotify2000 = pd.read_csv('../dataset/Spotify-2000/csv/Spotify-2000.csv')

spotify2000.drop("Index", inplace = True, axis = 1)

spotify2000.drop(spotify2000.iloc[:, 3:14], inplace = True, axis = 1)

spotify2000.columns = [ 
    "Title", 
    "Artist",  
    "Genre"
]

decade2000 = pd.read_csv('../dataset/Decades/csv/2000.csv')

decade2000.drop("Number", inplace = True, axis = 1)

decade2000.drop(decade2000.iloc[:, 3:14], inplace = True, axis = 1)

decade2000.columns = [ 
    "Title", 
    "Artist",  
    "Genre"
]

decade2010 = pd.read_csv('../dataset/Decades/csv/2010.csv')

decade2010.drop("Number", inplace = True, axis = 1)

decade2010.drop(decade2010.iloc[:, 3:14], inplace = True, axis = 1)

decade2010.columns = [ 
    "Title", 
    "Artist",  
    "Genre"
]

musicGenres = pd.concat([decade2000, decade2010, spotify2000])

musicGenres.drop_duplicates(keep = 'first', inplace = True)

#musicGenres.to_csv('../dataset/teste.csv', index=False)

merged = pd.merge(combinedLyrics, musicGenres, on=['Artist', 'Title'])

merged.drop_duplicates(keep = 'first', inplace = True)

#merged.groupby(['Artist', 'Title', 'Album', 'Date', 'Lyric']).sum()

final = merged.copy()
    
for indexM, rowM in merged.iterrows():
    if (rowM['Artist'] == 'Beyoncé'):
        artist = pd.read_csv('../dataset/Song-Lyrics-Dataset/csv/Beyonce.csv')
    else:
        artist = pd.read_csv('../dataset/Song-Lyrics-Dataset/csv/' + rowM['Artist'].replace(" ","") + '.csv')
    print(artist.head())
    for indexA, rowA in artist.iterrows():
        if rowM['Album'] == rowA['Album'] and rowM['Title'] != rowA['Title']:
            print('Found ' + rowA['Title'])
            final = final.append({'Artist' : rowA['Artist'],
                           'Title' : rowA['Title'],
                           'Album' : rowA['Album'],
                           'Date' : rowA['Date'],
                           'Lyric' : rowA['Lyric'],
                           'Genre' : rowM['Genre']}, ignore_index=True)
            
final.to_csv('../dataset/merged.csv', index=False)

