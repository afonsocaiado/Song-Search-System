import pandas as pd

def extend(data):
    final = data.copy()
    
    for indexM, rowM in data.iterrows():
        if (rowM['Artist'] == 'Beyoncé'):
            artist = pd.read_csv('../dataset/Song-Lyrics-Dataset/csv/Beyonce.csv')
        else:
            artist = pd.read_csv('../dataset/Song-Lyrics-Dataset/csv/' + rowM['Artist'].replace(" ","") + '.csv')
        
        for indexA, rowA in artist.iterrows():
            if rowM['Album'] == rowA['Album'] and rowM['Title'] != rowA['Title']:
                final = final.append({'Artist' : rowA['Artist'],
                               'Title' : rowA['Title'],
                               'Album' : rowA['Album'],
                               'Date' : rowA['Date'],
                               'Lyric' : rowA['Lyric'],
                               'Top Genre' : rowM['Top Genre']}, ignore_index=True)
    
    return final