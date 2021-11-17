import pandas as pd

if __name__ == '__main__':
    
    combined = pd.read_csv('dataset/combined.csv')
    
    combined = combined.drop(combined.iloc[:, 5:8], axis=1)
    combined = combined.drop(combined.iloc[:, 6:29], axis=1)
    
    combined.drop_duplicates(keep = 'first', inplace = True)
    
    combined.to_csv('dataset/clean.csv', index=False)
    
    print('Cleaned the data and wrote it to clean.csv\n')