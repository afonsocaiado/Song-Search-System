import pandas as pd

if __name__ == '__main__':
    
    data = pd.read_csv('dataset/clean.csv')
    
    final = data.copy()
    
    for indexM, rowM in final.iterrows():
        if (rowM['Artist'] == 'Beyoncé'):
            artist = pd.read_csv('dataset/Song-Lyrics-Dataset/csv/Beyonce.csv')
        else:
            artist = pd.read_csv('dataset/Song-Lyrics-Dataset/csv/' + rowM['Artist'].replace(" ","") + '.csv')
        
        for indexA, rowA in artist.iterrows():
            if rowM['Album'] == rowA['Album'] and rowM['Title'] != rowA['Title']:
                final = final.append({'Artist' : rowA['Artist'],
                               'Title' : rowA['Title'],
                               'Album' : rowA['Album'],
                               'Date' : rowA['Date'],
                               'Lyric' : rowA['Lyric'],
                               'Top Genre' : rowM['Top Genre']}, ignore_index=True)
                
    final.drop_duplicates(subset = ['Artist', 'Title', 'Album'], inplace = True)
    
    final['id'] = range(1, len(final) + 1)
    
    final.to_csv('solr/data/music_lyrics.csv', index=False)
    
    print('Extended the data and wrote it to music_lyrics.csv\n')