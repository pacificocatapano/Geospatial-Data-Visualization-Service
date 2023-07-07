# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:01:16 2023

@author: Sasym
"""
from streamlit_extras.switch_page_button import switch_page
import streamlit as st 
import requests
import os
import pandas as pd


st.set_page_config(layout="wide")
st.title("Interfaccia di visualizzazione dati geospaziali \U0001F30D")

url = 'http://192.168.1.22:5000/download'
destination = './ubx.csv'
response = requests.get(url)
response.raise_for_status()  # Controlla se la richiesta ha avuto successo
with open(destination, 'wb') as file:
    file.write(response.content)

df_llh = pd.read_csv("./ubx.csv", sep = ';')
df_status = pd.read_csv("./provaUBXstatus.csv", sep = ';')
df_ecef = pd.read_csv("./provaUBXecef.csv", sep = ';') 

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

df_llh_filtered = df_llh[time_filter_lower &  time_filter_upper]   
df_ecef_filtered = df_ecef[time_filter_lower &  time_filter_upper]   
df_status_filtered = df_status[time_filter_lower &  time_filter_upper]   


### Dataframe
if df_llh_filtered.shape[0] != 0:
    st.write('LLH')
    st.dataframe(df_llh_filtered,
                 use_container_width=True,
                 hide_index=True)

if df_status.shape[0] != 0:
    st.write('STATUS')
    st.dataframe(df_status_filtered,
                 use_container_width=True,
                 hide_index=True)

if df_ecef.shape[0] != 0:
    st.write('ECEF')
    st.dataframe(df_ecef_filtered,
                 use_container_width=True,
                 hide_index=True)