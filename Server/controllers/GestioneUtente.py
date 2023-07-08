from flask import render_template, request, session
from DB.DB import connectDB

def login():
    msg = ''
    if request.method == 'POST':
        Email = request.form['Email']
        Password = request.form['Password']
        connection = connectDB()
        account = connection.execute('SELECT * FROM Utenti WHERE Email = ? AND Password = ?', (Email, Password,)).fetchone()
        if account:
            session['loggedin'] = True
            session['username'] = account['Email']
            connection = connectDB()
            connection.close()
            return render_template('/data.html')
        else:
            msg = 'Credenziali inserite non valide!'
    return render_template('/Utente/login.html',msg=msg)

def register():
    msg = ''
    if request.method == 'POST':
        Email = request.form['Email']
        Password = request.form['Password']
        connection = connectDB()

        if not Email:
            msg = 'Email is required.'
        elif not Password:
            msg = 'Password is required.'

        if msg == '':
            try:
                connection.execute(
                    "INSERT INTO Utenti (Email, Password) VALUES (?, ?)",
                    # HASHING PASSWORD
                    (Email, Password),
                )
                connection.commit()
            
            except connection.IntegrityError:
                msg = f'Email {Email} è già registrato.'
                return render_template('Utente/register.html', msg=msg)
        
        return render_template('/Utente/login.html', msg=msg)

    return render_template('Utente/register.html', msg=msg)