# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:41:41 2023

@author: Sasym
"""

from flask import Flask, request, send_file, render_template, redirect, url_for
import os
import pandas as pd
import streamlit as st 

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')

#Gestione login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['email']
    password = request.form['password']

    # Esempio di controllo delle credenziali
    if username == 'admin' and password == 'password':
        return redirect(url_for('dati_page'))
    else:
        error_message = "Credenziali non valide. Riprova."
        return render_template('login.html', error_message=error_message)

# Pagina di visualizzazione dei dati
@app.route('/dati')
def dati_page():
    # Controlla l'autenticazione dell'utente qui
    # Se l'utente non è autenticato, puoi reindirizzarlo alla pagina di login

    return render_template('dati.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']  # Ottieni il file dalla richiesta
    # Fai qualcosa con il file (salvalo, elaboralo, ecc.)
    """
    csv = parsing(file)
    save_csv_in_database()
    """
    file.save(os.path.join('Salva', 'file.csv'))

    return 'File caricato con successo!'

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.22')