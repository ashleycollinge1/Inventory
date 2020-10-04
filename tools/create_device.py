import requests, json

json_data = {'name': 'test-name'}

request_data = requests.post('http://127.0.0.1:5000/api/device/', json=json_data)

print(request_data.status_code)
print(json.dumps(request_data.json(), indent=4))
