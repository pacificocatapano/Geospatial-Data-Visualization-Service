from flask import Blueprint
from controllers.GestioneUtente import *

GestioneUtente_bp = Blueprint('GestioneUtente_bp', __name__)

GestioneUtente_bp.route('/login', methods=["GET", "POST"])(login)
GestioneUtente_bp.route('/registrazione', methods=["GET", "POST"])(registrazione)
GestioneUtente_bp.route('/recupero_password', methods=["GET", "POST"])(recupero_password)
GestioneUtente_bp.route('/conferma_recupero_password', methods=["GET", "POST"])(conferma_recupero_password)
