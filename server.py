# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:41:41 2023

@author: Sasym
"""

from flask import Flask, request
import os
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
    file.save(os.path.join('Salva', 'file.txt'))
    return 'File caricato con successo!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')