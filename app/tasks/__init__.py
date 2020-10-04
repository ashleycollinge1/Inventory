from app import CELERY
from flask import jsonify

@CELERY.task
def first_task():
    return jsonify({"result": 1+1})
