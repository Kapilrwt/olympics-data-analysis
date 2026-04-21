
import os
import pandas as pd
import streamlit as st
from .config import BASE_DIR

# this functions are for app.py
@st.cache_data
def load_data():
    print(os.getcwd())
    projectPath = BASE_DIR
    afp = os.path.join(projectPath,'data','raw_data','athlete_events.csv') #athlete file path
    rfp = os.path.join(projectPath,'data','raw_data','noc_regions.csv') #region file path
    adf = load_athlete_data(afp)
    rdf = load_region_data(rfp)
    return adf , rdf

# this functions are for notebook
def load_athlete_data(fp):
    try:
        return pd.read_csv(fp)
    except FileNotFoundError:
        print(f'unable to find file at given location {fp}')
    except Exception as e:
        print(f'unable to load file due to {e}')

def load_region_data(fp):
    try:
        return pd.read_csv(fp)
    except FileNotFoundError:
        print(f'unable to find file at given location {fp}')
    except Exception as e:
        print(f'unable to load file due to f{e}')

load_data()

