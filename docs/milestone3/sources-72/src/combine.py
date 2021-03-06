import pandas as pd
import glob

if __name__ == '__main__':

    #Reading lyrics dataset
    file_extension = '.csv'
    all_filenames = [i for i in glob.glob(f"dataset/Song-Lyrics-Dataset/csv/*{file_extension}")]
    
    combinedLyrics = pd.concat([pd.read_csv(f, index_col=[0]) for f in all_filenames])  
    
    #Reading spotify playlist dataset
    spotifyTest = pd.read_csv('src/spotifyData.csv', index_col=[0])

    #Combine both
    merged = pd.merge(combinedLyrics, spotifyTest, on=['Artist', 'Title'])

    merged.to_csv('src/combined.csv', index=False)
    
    print('Combined the data and wrote it to combined.csv\n')