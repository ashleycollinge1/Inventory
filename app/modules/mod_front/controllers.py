import os
from flask import Blueprint, render_template, jsonify

MOD_FRONT = Blueprint('front', __name__, url_prefix='/')

@MOD_FRONT.route("/", methods=["GET"])
def index():
    """
    Main dashboard
    """
    return render_template('mod_front/index.html')

