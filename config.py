import os

DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DB_username = os.environ['POSTGRES_USER']
DB_password = os.environ['POSTGRES_PASS']
DB_hostname = os.environ['POSTGRES_HOST']
DB_name     = os.environ['POSTGRES_DB']
CELERY_BROKER_URL       = os.environ['CELERY_BROKER_URL']
CELERY_RESULT_BACKEND   = os.environ['CELERY_RESULT_BACKEND']

SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(DB_username, DB_password, DB_hostname, DB_name)

SQLALCHEMY_TRACK_MODIFICATIONS = False
CSRF_ENABLED = True
CSRF_SESSION_KEY = "secret"
SECRET_KEY = "secret"

