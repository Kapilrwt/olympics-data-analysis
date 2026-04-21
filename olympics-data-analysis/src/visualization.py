
import pandas as pd
import plotly.express as px
from plotly import figure_factory as ff

def nation_over_time_plot(df):
    
    fig = px.line(df,x='Year',y='Nations')
                  
    fig.update_layout(
        xaxis = dict(
            title = 'Year',
            showgrid = True,
            title_font = dict(
                size = 16
            )
        ),
        yaxis = dict(
            title = 'Nations',
            showgrid = True,
            title_font = dict(
                size = 16
            )
        )
    )

    return fig

def events_over_time_plot(df):
    
    fig = px.line(df , x = 'Year' , y = 'Events')

    fig.update_layout(
        xaxis = dict(
            title = 'Year',
            showgrid = True,
            title_font = dict(
                size = 16
            )
        ),
        yaxis = dict(
            title = 'Events',
            showgrid = True,
            title_font = dict(
                size = 16
            )
        )
    )

    return fig

def athleles_participation_over_time_plot(df):

    fig = px.line(df,x='Year',y='Athletes')
    
    fig.update_layout(
        xaxis = dict(
            title = 'Year',
            showgrid = True,
            title_font = dict(
                size = 16
            )
        ),
        yaxis = dict(
            title = 'Athletes',
            showgrid = True,
            title_font = dict(
                size = 16
            )
        )
    )

    return fig

def events_of_sports_with_time_freq_plot(df):

    fig = px.imshow(df)

    fig.update_layout(
        height=600,
        width=800,
        xaxis = dict(
            title = 'Year',
            title_font = dict(
                size = 16
            )
        ),
        yaxis = dict(
            title = 'Sports',
            title_font = dict(
                size = 16
            )
        )
    )

    return fig

def country_wise_medal_counts_plot(df):

    fig = px.line(df,x='Year',y='Medals')

    fig.update_layout(
        xaxis = dict(
            title = 'Year',
            title_font = dict(
                size = 16
            )
        ),
        yaxis = dict(
            title = 'Medals',
            title_font = dict(
                size = 16
            )
        )
    )

    return fig

    
def medals_count_In_sport_by_country_with_time_plot(df):

    fig = px.imshow(df)

    fig.update_traces(xgap=1, ygap=1)

    fig.update_layout(
        height=600,
        width=800,
        xaxis = dict(
            title = 'Year',
            title_font = dict(
                size = 16
            )
        ),
        yaxis = dict(
            title = 'Sports',
            title_font = dict(
                size = 16
            )
        )
    )

    return fig

def medal_distribution_plot(gm,sm,bm):
    fig = ff.create_distplot(
        hist_data=[gm,sm,bm],
        group_labels=['Gold Medalist','Silver Medalist','Bronze Medalist'],
        show_hist=False, 
        show_rug=False,
        colors=['Gold','Silver','Brown']
                             
    )
    fig.add_vline(gm.mean(),line_dash='dash',line_color='Gold')
    fig.add_vline(sm.mean(),line_dash='dash',line_color='Silver')
    fig.add_vline(bm.mean(),line_dash='dash',line_color='Brown')

    fig.update_layout(
        title = 'Medal Distribution',
        height=600,
        width=800,
        xaxis = dict(
            title = 'Age',
            title_font = dict(
                size = 16
            )
        ),
        yaxis = dict(
            title = 'Density',
            title_font = dict(
                size = 16
            )
        )
    )

    return fig

def age_distribution_plot(df):

    fig = ff.create_distplot([df],['Age Distribution'],show_curve=True,show_hist=False,show_rug=False)

    fig.add_vline(df.mean(),line_dash='dash',line_color='blue')

    fig.update_layout(
        title = 'Age Distribution',
        height=600,
        width=800,
        xaxis = dict(
            title = 'Age',
            title_font = dict(
                size = 16
            )
        ),
        yaxis = dict(
            title = 'Density',
            title_font = dict(
                size = 16
            )
        )
    )
    return fig 

def age_distribution_by_sports_plot(afs):

    updated_afs = dict()
    for key,value in afs.items():
        
        unique = set(value)
        if len(unique)>1:
            updated_afs[key]=value
    
    sports = list(updated_afs.keys())
    ages = list(updated_afs.values())
    
    
    fig = ff.create_distplot(ages,sports,show_rug=False,show_hist=False,show_curve=True)

    fig.update_layout(
        title = 'Age Distribution',
        height=600,
        width=800,
        xaxis = dict(
            title = 'Age',
            title_font = dict(
                size = 16
            )
        ),
        yaxis = dict(
            title = 'Density',
            title_font = dict(
                size = 16
            )
        )
    )

    return fig

def medal_dist_on_physiic_by_sport(df):
    
    fig = px.scatter(
    data_frame=df,
    x='Weight',
    y='Height',
    color='Medal',
    category_orders={
        'Medal': ['Gold','Silver','Bronze','No Medal']
    },
    color_discrete_map={
        'Gold': '#FFD700',
        'Silver': '#C0C0C0',
        'Bronze': '#CD7F32',
        'No Medal': '#80ffff'
    },
    opacity=0.7
    )

    fig.update_layout(
        title = 'Medal Distribution',
        height=600,
        width=800,
        xaxis = dict(
            title = 'Weight (In Kg)',
            title_font = dict(
                size = 16
            )
         ),
        yaxis = dict(
            title = 'Height (In Cm)',
            title_font = dict(
               size = 16
           )
        )
    )

    return fig 

def men_vs_women_parti_over_the_year_plot(df):

    y_column = df.columns.tolist()
    y_column.remove('Year')

    fig = px.line(data_frame=df,x='Year',y=y_column)

    fig.update_layout(
        title = 'Men Vs Women Participation',
        height=600,
        width=800,
        xaxis = dict(
            title = 'Year',
            title_font = dict(
                size = 16
            )
         ),
        yaxis = dict(
            title = 'Sex',
            title_font = dict(
               size = 16
           )
        )
    )

    return fig