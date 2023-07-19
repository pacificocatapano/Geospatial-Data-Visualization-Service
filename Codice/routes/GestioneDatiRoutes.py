from flask import Blueprint

from controllers.GestioneDati import *

GestioneDati_bp = Blueprint('GestioneDati_bp', __name__)

GestioneDati_bp.route('/dati', methods=["GET", "POST"])(dati)
GestioneDati_bp.route('/acquisisciDati', methods=['POST'])(acquisisciDati)
GestioneDati_bp.route('/get_latest_data', methods=['GET'])(get_latest_data)