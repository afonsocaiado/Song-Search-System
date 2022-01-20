import pandas as pd

if __name__ == '__main__':
    
    combined = pd.read_csv('src/combined.csv')
    
    combined = combined.drop(['Year'], axis=1)
    
    combined.to_csv('src/clean.csv', index=False)
    
    print('Cleaned the data and wrote it to clean.csv\n')