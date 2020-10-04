from app import DB

class Test(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    date_created = DB.Column(DB.DateTime, default=DB.func.current_timestamp())
    date_modified = DB.Column(DB.DateTime, default=DB.func.current_timestamp(),
            onupdate=DB.func.current_timestamp())

class Devices(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    date_created = DB.Column(DB.DateTime, default=DB.func.current_timestamp())
    date_modified = DB.Column(DB.DateTime, default=DB.func.current_timestamp(),
            onupdate=DB.func.current_timestamp())
    hostname = DB.String(DB.String(150))

