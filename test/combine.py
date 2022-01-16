import pandas as pd
import glob

if __name__ == '__main__':

    #Reading lyrics dataset
    file_extension = '.csv'
    all_filenames = [i for i in glob.glob(f"../dataset/Song-Lyrics-Dataset/csv/*{file_extension}")]
    
    combinedLyrics = pd.concat([pd.read_csv(f) for f in all_filenames])  
    
    #Reading spotify playlist dataset
    spotifyTest = pd.read_csv('spotifytest.csv')

    merged = pd.merge(combinedLyrics, spotifyTest, on=['Artist', 'Title'])

    merged.to_csv('combined.csv', index=False)
    
    print('Combined the data and wrote it to combined.csv\n')