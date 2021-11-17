import pandas as pd

def clean(data):
    data = data.drop(data.iloc[:, 5:8], axis=1)
    data = data.drop(data.iloc[:, 6:29], axis=1)
    
    data.drop_duplicates(keep = 'first', inplace = True)
    
    return data