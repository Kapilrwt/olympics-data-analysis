

import pandas as pd 
import streamlit as st
from src import helper as hp
from src import config as cfg
from src import analysis as an
from src import data_loader as dl
from src import preprocessing as pp
from src import visualization as vis

#cleaning data 
athlete_data  , region_data = dl.load_data()
df = pp.preprocess(athlete_data,region_data)

st.sidebar.title('Olympic Analysis')

st.sidebar.image(cfg.LOGO_PATH)

options = st.sidebar.radio(
    label = 'Select an Option',
    options = ['Medal Tally','Overall Analysis','Country-wise Analysis','Athlete-wise Analysis']
)


if(options=='Medal Tally'):
    st.sidebar.header('Medal Tally')

    #building dropdown here 
    country,year = hp.fetch_country_and_year(df)
    
    selected_country = st.sidebar.selectbox('Country',country)
    selected_year = st.sidebar.selectbox('Year',year)

    title = 'Overall Medal Tally'
    if(selected_country=='Overall' and selected_year=='Overall'):
        pass
    elif(selected_country!='Overall' and selected_year=='Overall'):
        title = f'Medal Tally of {selected_country}'
    elif(selected_country=='Overall' and selected_year!='Overall'):
        title = f'Medal Tally In {selected_year}'
    elif(selected_country!='Overall' and selected_year!='Overall'):
        title = f'Medal Tally of {selected_country} In {selected_year}'
    else:
        pass

    st.title(title)
    
    #building medal tally 
    medal_tally = pp.expanding_medal_column(df)             
    medal_tally = an.building_medal_tally_by_region(medal_tally,selected_country,selected_year)
    st.dataframe(medal_tally)

elif(options=='Overall Analysis'):

    st.title('Statistics')

    editions,hosts,sports,events,athletes,nations = an.olympic_analysis(df)

    col1 , col2, col3 = st.columns(3)
    with col1:
        st.header('Editions')
        st.subheader(str(editions))
    with col2:
        st.header('Hosts')
        st.subheader(str(hosts))
    with col3:
        st.header('Nations')
        st.subheader(str(nations))

    col1 , col2, col3 = st.columns(3)
    with col1:
        st.header('Sports')
        st.subheader(str(sports))
    with col2:
        st.header('Events')
        st.subheader(str(events))
    with col3:
        st.header('Athletes')
        st.subheader(str(athletes))

    st.write('')
    st.header('Participation of Nations Over the Years')
    nsot = hp.participating_country_over_time(df) #nsot - nations over time
    nsot_graph = vis.nation_over_time_plot(nsot)
    st.plotly_chart(nsot_graph)

    st.header('No. of  Events Over Time')
    efot = hp.events_freq_over_time(df)
    efot_graph = vis.events_over_time_plot(efot)
    st.plotly_chart(efot_graph)

    st.header('Participation of Athletes Over Time')
    afot = hp.athletes_freq_over_time(df)
    afot_fig = vis.athleles_participation_over_time_plot(afot)
    st.plotly_chart(afot_fig)

    st.header('No. of Events for Sports Over the Time')
    ues = hp.events_freq_of_sports_with_time(df)
    ues_plot = vis.events_of_sports_with_time_freq_plot(ues)
    st.plotly_chart(ues_plot)

    st.header('Most Successfull Athletes of all Time')
    sports = hp.fetch_sports(df)
    selected_sport = st.selectbox('Sport',sports)
    top_performer = an.top_athletes(df,selected_sport)
    st.dataframe(top_performer)

elif(options=='Country-wise Analysis'):

    country = hp.fetch_country_with_india_on_top(df)
    selected_country = st.sidebar.selectbox(label='Select Country' , options=country)

    st.header(f'Medal Won by {selected_country} Over the Years')
    cwmt = hp.country_wise_medals_count_with_time(df,selected_country) #cwmt - country-wise medal tally
    cwmt_plot = vis.country_wise_medal_counts_plot(cwmt)
    st.plotly_chart(cwmt_plot)

    st.header(f'Medal Won In Sports by {selected_country} Over the Years')
    cwmcis = hp.medal_counts_by_country_In_sport(df,selected_country) #cwmcis = country wise medal count in sport
    cwmcis_fig = vis.medals_count_In_sport_by_country_with_time_plot(cwmcis)
    st.plotly_chart(cwmcis_fig)
    
    st.header(f'Top Athletes of {selected_country}')
    sports = hp.fetch_sports(df)
    selected_sport = st.selectbox('Select Sport',sports)
    dfoc = hp.filter_df_by_country(df,selected_country) #dfoc - dataframe of country
    ta = an.top_athletes(dfoc,selected_sport) #ta - top athletes
    st.dataframe(ta)

elif(options=='Athlete-wise Analysis'):
    
    st.header('Age Distribution of Athletes')
    age = hp.fetch_age(df)
    age_dist_fig = vis.age_distribution_plot(age)
    st.plotly_chart(age_dist_fig)

    st.header('Age Distribution of Athletes based on Sport')
    afs = hp.fetch_athlets_age_by_sport(df) #afs - ages of athletes from sports
    afs_fiq = vis.age_distribution_by_sports_plot(afs)
    st.plotly_chart(afs_fiq)

    st.header('Medal Distribution of Athletes')
    gm,sm,bm = hp.seprate_medalists(df)
    medal_dist_fig = vis.medal_distribution_plot(gm,sm,bm)
    st.plotly_chart(medal_dist_fig)

    st.header('Medal Distribution based on Height-Weight')
    sports = hp.fetch_sports(df)
    options01 = st.selectbox('Select Sports',sports)
    mdopbs = hp.athlete_measurment_by_sport(options01,df)   #mdopbs - medal distribution on physiic by sport
    mdopbs_fig = vis.medal_dist_on_physiic_by_sport(mdopbs)
    st.plotly_chart(mdopbs_fig)

    st.header('Men vs Women Participation Over the Year')
    options02 = st.selectbox('Select Sport',sports)
    swdoty = hp.men_vs_women_parti_over_the_year(options02,df)  #sex wise distribution over the years
    swdoty_fig = vis.men_vs_women_parti_over_the_year_plot(swdoty)
    st.plotly_chart(swdoty_fig)

else:
    pass


