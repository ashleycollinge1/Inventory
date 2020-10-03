import os

DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://@127.0.0.1/inventory'
SQLALCHEMY_TRACK_MODIFICATIONS = False
CSRF_ENABLED = True
CSRF_SESSION_KEY = "secret"
SECRET_KEY = "secret"

