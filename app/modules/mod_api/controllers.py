import os
from flask import Blueprint, render_template, jsonify

MOD_API = Blueprint('api', __name__, url_prefix='/api/',
                                      static_folder='static/mod_api', static_url_path='static')

@MOD_API.route("/test/", methods=["GET"])
def test():
    """
    .. :quickref: API; Test endpoint
    .. http:get:: /test/

    Quick and simple GET request to see if it's live

       **Example request**:

       .. sourcecode:: http

            GET /users/123/posts/web HTTP/1.1
            Host: example.com
            Accept: application/json, text/javascript

        **Example response**:

        .. sourcecode:: http

            HTTP/1.1. 200 OK
            Vary: Accept
            Content-Type: text/javascript

            [
                {
                    "Return": "success",
                    "message": "Everything is okay",
                    "os.environ": "username"
                }
            ]
    """
    return jsonify({"Return": "success", "message": "Everything is okay",
        "os.environ": os.environ['POSTGRES_USER']})

@MOD_API.route("/devices/", methods=['GET'])
def get_all_devices():
    """
    .. todo:: Going to do more stuff here
    """
