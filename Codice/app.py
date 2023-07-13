from DB.DB import initDB
from flask import Flask, render_template
from routes.GestioneUtenteRoutes import GestioneUtente_bp
from routes.GestioneDatiRoutes import GestioneDati_bp

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(GestioneUtente_bp, url_prefix='/')
app.register_blueprint(GestioneDati_bp, url_prefix='/')

initDB()

# ---------------------- HOMEPAGE ----------------------
@app.route('/')
def home():
    return render_template('homepage.html')

# ---------------------- UTENTE ----------------------
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registrazione')
def registrazione():
    return render_template('registrazione.html')

@app.route('/recupero_password')
def recupero_password():
    return render_template('recupero_password.html')

@app.route('/conferma_recupero_password')
def conferma_recupero_password():
    return render_template('conferma_recupero_password.html')

# ---------------------- DATI ----------------------
@app.route('/dati')
def dati():
    return render_template('dati.html')

@app.route('/acquisisciDati')
def acquisisciDati():
    return 'Acquisizione dati'

<<<<<<< Updated upstream
=======
@app.route('/logout')
def logout():
    print("trapanaturo")
    #return render_template('login.html')
    return redirect(url_for('login'))

>>>>>>> Stashed changes
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
    
