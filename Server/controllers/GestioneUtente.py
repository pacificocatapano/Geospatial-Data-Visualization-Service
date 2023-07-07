from flask import render_template, request, session
from DB.DB import connectDB

def login():
    msg = ''
    if request.method == 'POST':
        Email = request.form['Email']
        Password = request.form['Password']
        connection = connectDB()
        account = connection.execute('SELECT * FROM Utenti WHERE Email = ? AND PWD = ?', (Email, Password,)).fetchone()

        if account:
            session['loggedin'] = True
            session['username'] = account['Email']
            connection = connectDB()
            connection.close()
            msg = f'Benvenuto {Email}!'
        else:
            msg = 'Credenziali inserite non valide!'
    return render_template('/Utente/login.html',msg=msg)

def register():
    if request.method == 'POST':
        Email = request.form['Email']
        Password = request.form['Password']
        connection = connectDB()
        error = None

        if not Email:
            error = 'Email is required.'
        elif not Password:
            error = 'Password is required.'

        if error is None:
            try:
                connection.execute(
                    "INSERT INTO user (Email, Password) VALUES (?, ?)",
                    # HASHING PASSWORD
                    (Email, Password),
                )
                connection.commit()
            except connection.IntegrityError:
                error = f"Email {Email} is already registered."

    return render_template('Utente/register.html')