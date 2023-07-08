from flask import render_template, request, redirect, url_for, session
from DB.DB import connectDB
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
    msg = ''
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        connection = connectDB()
        account = connection.execute('SELECT * FROM Utenti WHERE Email = ? AND Password = ?', (email, password,)).fetchone()

        if account:
            session['loggedin'] = True
            session['username'] = account['Email']
            connection = connectDB()
            connection.close()
            return redirect(url_for('dati'))
        else:
            msg = 'Credenziali inserite non valide!'
            connection.close()
            return render_template('login.html', msg=msg)
    
    return render_template('login.html', msg=msg)

def registrazione():
    msg = ''
    if request.method == 'POST':
        # Ottieni i dati dal modulo di registrazione
        nome = request.form['nome']
        cognome = request.form['cognome']
        email = request.form['email']
        password = request.form['password']
        connection = connectDB()

        # CONTROLLO EMAIL
        try:
            connection.execute(
                "INSERT INTO Utenti (Nome, Cognome, Email, Password) VALUES (?, ?, ?, ?)",
                (nome, cognome, email, password),
            )
            connection.commit()
            connection.close()
        except connection.IntegrityError:
            msg = f'L\'utente {email} è già registrato.'
            connection.close()
            return render_template('registrazione.html', msg=msg)

        # Reindirizza l'utente a una pagina di conferma o alla pagina di login
        return redirect(url_for('login'))

    return render_template('registrazione.html', msg=msg)

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