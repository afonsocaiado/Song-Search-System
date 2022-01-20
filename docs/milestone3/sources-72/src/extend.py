import pandas as pd

if __name__ == '__main__':
    
    data = pd.read_csv('src/clean.csv')
    
    final = data.copy()
    
    final['id'] = range(1, len(final) + 1)
    
    final.to_csv('solr/data/music_lyrics.csv', index=False)
    
    print('Extended the data and wrote it to music_lyrics.csv\n')