import pandas as pd

def building_medal_tally_by_region(df,country,year):

    by_year = False
    mtdf = df.drop_duplicates(subset=['Year','Sport','Event','Team','Games','City','Medal','NOC'])

    if(country=='Overall' and year=='Overall'):
        pass
    elif(country!='Overall' and year=='Overall'):
        by_year = True
        mtdf = mtdf[mtdf['region']==country]
    elif(country=='Overall' and year!='Overall'):
        mtdf = mtdf[mtdf['Year']==year]
    elif(country!='Overall' and year!='Overall'):
        mtdf = mtdf[(mtdf['region']==country) & (mtdf['Year']==year)]
    else:
        pass
        
    if(by_year):
        medal_tally = mtdf.groupby(by=['Year'])[['Gold','Silver','Bronze']].sum().sort_values('Year',ascending=False).reset_index()
    else:
        medal_tally = mtdf.groupby(by=['region'])[['Gold','Silver','Bronze']].sum().sort_values('Gold',ascending=False).reset_index()
        
    medal_tally['Total'] = medal_tally['Gold']+medal_tally['Silver']+medal_tally['Bronze']
    medal_tally.index  = medal_tally.index + 1
    
    return medal_tally

def olympic_analysis(df):
    edition = df['Year'].unique().shape[0] - 1 #as olympic does not consider 1906 edition 
    hosts = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['ID'].unique().shape[0]
    nations = df['region'].unique().shape[0]
    return edition,hosts,sports,events,athletes,nations

def top_athletes(df,sport):
    df = df.dropna(subset = ['Medal'])
    if(sport=='Overall'):
        pass
    else:
        df = df[df['Sport']==sport]
    topdf = df['ID'].value_counts().reset_index(name='Medals')
    top_df = pd.merge(topdf,df,on='ID',how='left')[['Name','Sport','region','Medals']]
    top_df = top_df.drop_duplicates().reset_index(drop=True)
    top_df.index = top_df.index+1
    return top_df
    