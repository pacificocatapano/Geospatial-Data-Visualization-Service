# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 17:16:51 2023

@author: pacif
"""

# Per farlo partire digitare su terminale anaconda streamlit run bozza_fronte-end.py

import pandas as pd
import streamlit as st 
import os
import yaml

import pickle
from pathlib import Path

import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator


st.set_page_config(layout="wide")

credentials = {
    "usernames":{
        "osimhen":{
            "name":"Victor Osimhen",
            "password":"ok"
        }
    }
}


authenticator = stauth.Authenticate(credentials,cookie_name = 'abcdef', key = "abcdef",cookie_expiry_days = 0)
authenticator._register_credentials(username = "osimhen",name=  "victor", password = "ok", email = "ba@a", preauthorization = False)
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    st.title("Interfaccia di visualizzazione dati geospaziali \U0001F30D")

    # ---- READ EXCEL ----
    df_llh = pd.read_csv("./provaUBXllh.csv", sep = ';')
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

    # ---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)





