from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
DB = SQLAlchemy(app)
from app.modules.mod_api.models import Test

from app.modules.mod_front.controllers import MOD_FRONT
from app.modules.mod_api.controllers import MOD_API

app.register_blueprint(MOD_FRONT)
app.register_blueprint(MOD_API)

DB.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
