from flask import Blueprint, render_template, jsonify

MOD_FRONT = Blueprint('front', __name__, url_prefix='/',
                              static_folder='static/mod_agent', static_url_path='static')

@MOD_FRONT.route("/test/", methods=["GET"])
def test():
    """
    Test endpoint, just returns a success message
    """
    return jsonify({"Return": "success"})

