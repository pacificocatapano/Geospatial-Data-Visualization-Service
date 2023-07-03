# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 17:16:51 2023

@author: pacif
"""

# Per farlo partire digitare su terminale anaconda streamlit run bozza_fronte-end.py

import pandas as pd
import streamlit as st 
import os



st.set_page_config(layout="wide")


st.title("Interfaccia di visualizzazione dati geospaziali \U0001F30D")


df_llh = pd.read_csv("./provaUBXllh.csv", sep = ';')
df_status = pd.read_csv("./provaUBXstatus.csv", sep = ';')

### Filter sidebar
st.sidebar.header("Filters")

## TIME FILTER
timestamp_arr = list(df_llh['iTOW'])
timestamp_selected = st.sidebar.slider(
    label = 'iTOW', 
    min_value = min(timestamp_arr), 
    max_value = max(timestamp_arr), 
    value = [min(timestamp_arr), max(timestamp_arr)]
)

time_filter_lower = df_llh['iTOW'] >= timestamp_selected[0] 
time_filter_upper = df_llh['iTOW'] <= timestamp_selected[1]

df_filtered = df_llh[time_filter_lower &  time_filter_upper]   


### Dataframe
st.write('LLH')
st.dataframe(df_filtered, use_container_width = True)

st.write('STATUS')
st.dataframe(df_status, use_container_width = True)
