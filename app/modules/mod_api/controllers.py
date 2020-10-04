from flask import Blueprint, render_template, jsonify, request
from app import DB
from app.modules.mod_api.models import Device

MOD_API = Blueprint('api', __name__, url_prefix='/api/', static_folder='static/mod_api', static_url_path='static')

@MOD_API.route('/status/', methods=['GET'])
def get_status():
    """
    Returns the status of the API.

    Simple return saying 'success' for now  
    """
    return jsonify({'ping': 'pong'})

@MOD_API.route('/device/', methods=['GET'])
def get_devices():
    """
    Returns a list of all devices formatted in JSON
    """
    devices = DB.session.query(Device).all()
    devices_json = []
    if devices:
        for device in devices:
            device_json = {}
            device_json['id'] = device.id
            device_json['name'] = device.name
            device_json['date_created'] = device.date_created
            device_json['date_modified'] = device.date_modified
            device_json['hostname'] = device.hostname
            # ..TODO:: Need to use flask vars to create uri below, this is rubbish
            device_json['device_uri'] = 'http://127.0.0.1:5000/api/device/{}/'.format(device.id)
            devices_json.append(device_json)
    return jsonify(devices_json)

@MOD_API.route('/device/<device_id>/', methods=['GET'])
def get_device(device_id):
    """
    Retrieve specific device, returns all attrs of obj
    """
    query_results = DB.session.query(Device).filter_by(id=device_id).one()
    print(query_results.__dict__)
    properties = {}
    for i in query_results.__dict__:
        if i != '_sa_instance_state': # exclude sqlalchemy state
            properties[i] = query_results.__dict__[i]
    return jsonify(properties)

@MOD_API.route('/device/', methods=['POST'])
def new_device():
    """
    POST request to add a new device
    """
    json_data = request.get_json(force=True)
    new_device = Device()
    new_device.name = "Test-Name"
    new_device.hostname = "test-hostname"
    DB.session.add(new_device)
    try:
        DB.session.commit()
        return jsonify({'status': 'success', 'device_id': new_device.id})
    except:
        return jsonify({'status': 'failed', 'message': 'Undetermined reason'}), 500

