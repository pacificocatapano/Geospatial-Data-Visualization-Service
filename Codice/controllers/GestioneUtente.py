from flask import render_template, request, redirect, url_for, session
from DB.DB import connectDB
import random
import string
import os
import sendgrid
from sendgrid.helpers.mail import Mail

def create_text_email(email, reset_link):
    from_email = 'progettoSAD@outlook.com'
    to_email = email
    subject = 'Reset Your Password'
    message = f'''
    Hi,
    We received a request to reset your password. Click on the link below to reset it:
    {reset_link}
    If you didn't request a password reset, please ignore this email.
    Best regards,
    Your Website Team
    '''
    msg = Mail(
       from_email=from_email,
       to_emails=to_email,
       subject=subject,
       plain_text_content=message
    )
    return msg

def send_email(msg, email):
    sendgrid_api_key = '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'
    sg = sendgrid.SendGridAPIClient(api_key=sendgrid_api_key)
    try:
        response = sg.send(msg)
        if response.status_code == 202:
            print('Email sent successfully!')
        else:
            print('Error sending email:', response.body)
    except Exception as e:
        print('Error sending email:', str(e))
        


def email_valida(email):
    print(email)
    connection = connectDB()
    # CONTROLLO EMAIL
    Utente = connection.execute('SELECT * FROM Utenti WHERE Email = ?', (email,)).fetchone()
    if Utente is None:
        return False
    return True

def generatore_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return password

"""
AGGIUSTARE IL LINK O METTERE UNA PASSWORD GENERATA CASUALMENTE
"""
def invia_email_recupero_password(email, password):
    message = create_text_email(email, 'http://192.168.1.22:5000/registrazione')
    print(message)
    send_email(message, email)


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
            return render_template('login.html', msg=msg), 401
    
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
            return render_template('registrazione.html', msg=msg), 400

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
        return render_template('recupero_password.html', error_message=error_message), 400

    return render_template('recupero_password.html')

def conferma_recupero_password():
    return render_template('conferma_recupero_password.html')