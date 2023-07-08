from flask import Blueprint
from controllers.GestioneDati import *

GestioneDati_bp = Blueprint('GestioneDati_bp', __name__)

GestioneDati_bp.route('/dati', methods=["GET", "POST"])(dati)
