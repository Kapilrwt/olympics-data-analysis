import pandas as pd

#this func is build for app.py
def preprocess(adf,rdf):
    df = merge_athletes_to_region(adf,rdf)
    df = fetch_summer_olympics(df)
    df = remove_duplicate_rows(df)
    return df

#these functions are build for notebook
def merge_athletes_to_region(adf,rdf):
    return pd.merge(adf,rdf,on='NOC',how='left')
 
def fetch_summer_olympics(df):
    return df[df['Season']=='Summer']

def remove_duplicate_rows(df):
    return df.drop_duplicates()

#common function used by notebook and app.py 
def expanding_medal_column(df):
    dist = pd.get_dummies(df['Medal'])
    return pd.concat([df,dist] ,axis=1)