# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:44:57 2023

@author: Sasym
"""

import streamlit as st 
import subprocess

def esegui_login_page():
    comando = ["streamlit", "run", "login_page.py"]
    subprocess.run(comando)
    
st.title("registrazione utente")
nome = st.text_input("Nome")
cognome = st.text_input("Cognome")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
register_button = st.button("Conferma registrazione")

if register_button:
    st.success("Registrazione completata con successo!")
    esegui_login_page()