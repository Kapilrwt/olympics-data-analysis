#this file contains the helper function for analysis and eda

def fetch_sports(df):
    sports = df['Sport'].dropna().unique().tolist()
    sports.sort()
    sports.insert(0,'Overall')
    return sports

def fetch_country_and_year(df):
    country = df['region'].dropna().unique().tolist()
    country.sort()
    country.insert(0,'Overall')
    year = df['Year'].dropna().unique().tolist()
    year.sort()
    year.insert(0,'Overall')
    return country , year

def team_wise_df(df):
    df = df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
    return df

def participating_country_over_time(df):
    nsot = df.groupby('Year')['region'].nunique() #nsot - nations over time
    nsot = nsot.reset_index(name = 'Nations')
    return nsot

def events_freq_over_time(df):
    efot = df.groupby('Year')['Event'].nunique() #efot - events frequency over time
    efot = efot.reset_index(name = 'Events')
    return efot

def athletes_freq_over_time(df):
    paot = df.groupby('Year')['ID'].nunique() #paot - participating athletes over time
    paot = paot.reset_index(name='Athletes')
    return paot

def events_freq_of_sports_with_time(df):
    ues = df.drop_duplicates(subset=['Year','Sport','Event']) #ues - unique events
    ues_pivot = ues.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count',fill_value=0)
    return ues_pivot

def medal_counts_by_country_In_sport(df,country):
    df = df.dropna(subset=['Medal'])
    twdf = team_wise_df(df) #twdf - team wise data frame
    twdfoc = twdf[twdf['region']==country] #twdfoc - team wise data frame of country
    twdfoc_pivot = twdfoc.pivot_table(index='Sport',columns='Year',values='Medal',aggfunc='count',fill_value=0)
    return twdfoc_pivot


def country_wise_medals_count_with_time(df,country):
    df['Medal'].fillna('0',inplace=True)  #cwmt - country-wise medal tally
    cwmt = team_wise_df(df)
    cwmt = cwmt[cwmt['region']==country]
    cwmt = cwmt.groupby('Year')['Medal'].count()
    cwmt = cwmt.reset_index(name='Medals')
    return cwmt

def fetch_country_with_india_on_top(df):
    country = df['region'].dropna().unique()
    country = country.tolist()
    country.remove('India')
    country.sort()
    country.insert(0,'India')
    return country

def filter_df_by_country(df,country):
    df = df[df['region']==country]
    return df

def fetch_age(df):
    ua = df.drop_duplicates() #ua - unique athletes
    age = ua['Age'].dropna()
    return age

def seprate_medalists(df):
    df = df[df['Medal'].notna()]
    df = df.dropna(subset='Age')
    gm = df[df['Medal']=='Gold']['Age']
    sm = df[df['Medal']=='Silver']['Age']
    bm = df[df['Medal']=='Bronze']['Age']
    return gm,sm,bm

def fetch_athlets_age_by_sport(df):
    sports = df['Sport'].dropna().unique()
    sports = sports.tolist()
    sports.sort()
    afs = dict() #afs - athletes from given sport
    for sport in sports:
        afs_df = df[df['Sport']==sport] 
        ages = afs_df['Age'].dropna().tolist()
        afs[sport] = ages
    return afs

def athlete_measurment_by_sport(sport,df):
    if(sport!='Overall'):
        df = df[df['Sport']==sport]
    df = df.dropna(subset=['Height','Weight'])
    df['Medal'] = df['Medal'].fillna('No Medal')
    df['Medal'] = df['Medal'].astype(str)
    return df


def men_vs_women_parti_over_the_year(sport,df):
    if(sport!='Overall'):
        df = df[df['Sport']==sport]
    df = df.dropna(subset=['Sex'])

    wdf = df.pivot_table(index='Year',columns='Sex',values='ID',aggfunc='count')
    wdf = wdf.fillna(0).reset_index()
    return wdf
