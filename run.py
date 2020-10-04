from app import app
from app import DB

DB.create_all()
app.run(host='0.0.0.0')


