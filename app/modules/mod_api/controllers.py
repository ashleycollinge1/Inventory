from flask import Blueprint, render_template, jsonify

MOD_API = Blueprint('api', __name__, url_prefix='/api/', static_folder='static/mod_api', static_url_path='static')

@MOD_API.route('/status/', methods=['GET'])
def get_status():
    """
    Returns the status of the API.

    Simple return saying 'success' for now
    """
    return jsonify({'ping': 'pong'})

