from app import DB

class Device(DB.Model):
    id              = DB.Column(DB.Integer, primary_key=True)
    date_created    = DB.Column(DB.DateTime, default=DB.func.current_timestamp())
    date_modified   = DB.Column(DB.DateTime, default=DB.func.current_timestamp(),
            onupdate=DB.func.current_timestamp())
    name            = DB.Column(DB.String(150))
    device_type     = DB.Column(DB.String(100)) # win
    os_version      = DB.Column(DB.String(50)) # winxp win7 win8 win10
    hostname        = DB.Column(DB.String(100))
    CpuCorePhys     = DB.Column(DB.Integer)
    CpuCoreLog      = DB.Column(DB.Integer)
    MemoryMB        = DB.Column(DB.Integer)
    IPv4Address     = DB.Column(DB.String(16))
    MacAdd          = DB.Column(DB.String(12))
    LastLoggedOnBy  = DB.Column(DB.String(100))
    Manufacturer    = DB.Column(DB.String(100))
    Model           = DB.Column(DB.String(100))
    C_Used_Size_Mb  = DB.Column(DB.Integer)
    C_Total_Size_Mb = DB.Column(DB.Integer)

