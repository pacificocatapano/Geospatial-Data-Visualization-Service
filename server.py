<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:41:41 2023

@author: Sasym
"""

from flask import Flask, request, send_file
import os
import pandas as pd
import streamlit as st 

app = Flask(__name__)

@app.route('/')
def index():
    
    return 'Hello world'

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

@app.route('/download', methods=['GET'])
def download_file():
    return send_file('Salva/file.csv')

if __name__ == '__main__':
=======
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:41:41 2023

@author: Sasym
"""

from flask import Flask, request, send_file
import os
import pandas as pd
import streamlit as st 

app = Flask(__name__)

@app.route('/')
def index():
    
    return 'Hello world'

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

@app.route('/download', methods=['GET'])
def download_file():
    return send_file('Salva/file.csv')

if __name__ == '__main__':
>>>>>>> 1ba99e9cf47c8ac2c99699cf6481935c230ae9ea
    app.run(debug=True, host='192.168.1.22')