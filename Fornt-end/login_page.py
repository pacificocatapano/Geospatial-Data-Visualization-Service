# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:00:30 2023

@author: Sasym
"""

import streamlit as st 
import subprocess

def esegui_data_page():
    comando = ["streamlit", "run", "data_page.py"]
    subprocess.run(comando)


def esegui_register_page():
    comando = ["streamlit", "run", "register_page.py"]
    subprocess.run(comando)    
# Esegui script2.py

#LOGIN PAGE
st.title("Login utente")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
login_button = st.button("Login")
register_button = st.button("Registrazione")

if login_button:
# Verifica le credenziali dell'utente
    if email == "admin@example.com" and password == "password":
        st.success("Login successful!")
        esegui_data_page()   
    else:
        st.error("Invalid email or password")

if register_button:
    esegui_register_page()
