# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 12:19:26 2023

@author: Sasym
"""

import requests

# URL del server per l'upload del file
url = 'http://100.103.0.167:5000/upload'

# Path del file da inviare
file_path = 'file.txt'

# Esegui la richiesta POST
with open(file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post(url, files=files)

# Stampa la risposta
print(response.text)