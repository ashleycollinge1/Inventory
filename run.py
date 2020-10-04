from app import APPLICATION
from app import DB

DB.create_all()
APPLICATION.run(host='0.0.0.0')


