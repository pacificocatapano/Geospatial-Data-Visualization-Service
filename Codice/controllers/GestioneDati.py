from flask import render_template, session, redirect, url_for

def dati():
    # Esempio di dati per le tabelle

    if 'loggedin' in session:
        dati_ecef = [
            {'colonna1': 'Valore 1', 'colonna2': 'Valore 2', 'colonna3': 'Valore 3', 'colonna4': 'Valore 4', 'colonna5': 'Valore 5', 'colonna6': 'Valore 6', 'colonna7': 'Valore 7', 'colonna8': 'Valore 8', 'colonna9': 'Valore 9'},
            # Altri dati...
        ]

        dati_ssl = [
            {'colonna1': 'Valore 1', 'colonna2': 'Valore 2', 'colonna3': 'Valore 3', 'colonna4': 'Valore 4', 'colonna5': 'Valore 5', 'colonna6': 'Valore 6', 'colonna7': 'Valore 7', 'colonna8': 'Valore 8', 'colonna9': 'Valore 9'},
            # Altri dati...
        ]

        stati = [
            {'colonna1': 'Valore 1', 'colonna2': 'Valore 2', 'colonna3': 'Valore 3', 'colonna4': 'Valore 4', 'colonna5': 'Valore 5'},
            # Altri dati...
        ]

        return render_template('dati.html', dati_ecef=dati_ecef, dati_ssl=dati_ssl, stati=stati)

    return redirect(url_for('login'))