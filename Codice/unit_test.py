import pytest
from app import app

@pytest.fixture
def client():
    
    app.config["TESTING"] = True
    app.testing = True

    client = app.test_client()
    with app.app_context():
        yield client

#-------- REGISTRAZIONE --------
def test_registrazione_corretto(client):

    credenziali = {
        'nome' : 'Fabio',
        'cognome' : 'Boccia',
        'email': 'fabboccia@gmail.com',
        'password' : 'fabioboccia2000' 
    }

    rv = client.post("/registrazione", data=credenziali)
    assert rv.status_code == 302

def test_registrazione_sbagliato(client):

    credenziali = {
        'nome' : 'Fabio',
        'cognome' : 'Boccia',
        'email': 'fabboccia@gmail.com',
        'password' : 'fabioboccia2000' 
    }

    rv = client.post("/registrazione", data=credenziali)
    assert rv.status_code == 400

#-------- LOGIN --------
def test_login_corretto(client):

    credenziali = {
        'email': 'fabboccia@gmail.com',
        'password' : 'fabioboccia2000' 
    }

    rv = client.post("/login", data=credenziali)
    assert rv.status_code == 302

def test_login_sbagliato(client):

    credenziali = {
        'email': 'simone@gmail.com',
        'password' : 'fabioboccia2000' 
    }

    rv = client.post("/login", data=credenziali)
    assert rv.status_code == 401

#-------- RECUPERO PASSWORD --------
def test_recupero_password_corretto(client):

    credenziali = {
        'email': 'fabboccia@gmail.com',
    }

    rv = client.post("/recupero_password", data=credenziali)
    assert rv.status_code == 302

def test_recupero_password_sbagliato(client):

    credenziali = {
        'email': 'simone@gmail.com',
    }

    rv = client.post("/recupero_password", data=credenziali)
    assert rv.status_code == 400