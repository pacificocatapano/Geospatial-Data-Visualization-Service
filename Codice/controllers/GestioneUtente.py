from flask import render_template, request, redirect, url_for
import random
import string

def email_valida(email):
    return True

def generatore_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return password

def invia_email_recupero_password(email, password):
    return

# -----------------------

def login():
    if request.method == 'POST':

        username = request.form['email']
        password = request.form['password']

        # Esempio di controllo delle credenziali
        if username == 'admin@live.it' and password == 'password':
            return redirect(url_for('dati'))
        else:
            error_message = "Credenziali non valide. Riprova."
            return render_template('login.html', error_message=error_message)
    
    return render_template('login.html')

def registrazione():
    if request.method == 'POST':
        # Ottieni i dati dal modulo di registrazione
        nome = request.form['nome']
        cognome = request.form['cognome']
        email = request.form['email']
        password = request.form['password']

        # Esegui la logica di controllo per la registrazione
        # Qui puoi verificare l'unicità dell'email, fare controlli sui campi, salvare i dati nel database, ecc.

        # Reindirizza l'utente a una pagina di conferma o alla pagina di login
        return redirect(url_for('login'))

    return render_template('registrazione.html')

def recupero_password():
    if request.method == 'POST':
        email = request.form['email']

        # Verifica se l'email esiste nel database o in una lista di utenti registrati

        if email_valida(email):
            # Genera una password casuale
            nuova_password = generatore_password()

            # Simula l'invio della nuova password all'indirizzo email
            invia_email_recupero_password(email, nuova_password)

            # Reindirizza l'utente a una pagina di conferma
            return redirect(url_for('conferma_recupero_password'))

        error_message = "Email non valida"
        return render_template('recupero_password.html', error_message=error_message)

    return render_template('recupero_password.html')

def conferma_recupero_password():
    return render_template('conferma_recupero_password.html')