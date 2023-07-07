from flask import Flask, render_template

from routes.GestioneUtenteRoutes import GestioneUtente_bp

from DB.DB import initDB

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(GestioneUtente_bp, url_prefix='/')

#initDB()

@app.route('/')
def index():
    return 'Homepage'

# ----------------------- GESTIONE UTENTE -----------------------
@app.route('/login')
def login():
    return render_template('/Utente/login.html')

@app.route('/register')
def register():
    return render_template('/Utente/register.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')