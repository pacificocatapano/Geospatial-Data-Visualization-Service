from flask import Blueprint
from controllers.GestioneUtente import *

GestioneUtente_bp = Blueprint('GestionePazienteRegistrato_bp', __name__)

GestioneUtente_bp.route('/login', methods=["GET", "POST"])(login)
GestioneUtente_bp.route('/register', methods=["GET", "POST"])(register)