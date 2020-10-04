from flask import Flask
from celery import Celery
from flask_sqlalchemy import SQLAlchemy

APPLICATION = Flask(__name__)
APPLICATION.config.from_object('config')
DB = SQLAlchemy(APPLICATION)
CELERY = Celery('tasls', broker=APPLICATION.config['CELERY_BROKER_URL'])
CELERY.conf.update(APPLICATION.config)
from app.modules.mod_api.models import Device

from app.modules.mod_front.controllers import MOD_FRONT
from app.modules.mod_api.controllers import MOD_API

APPLICATION.register_blueprint(MOD_FRONT)
APPLICATION.register_blueprint(MOD_API)

DB.create_all()

if __name__ == "__main__":
    APPLICATION.run(host='0.0.0.0')
