import requests

r_json = {
    "name": "xgx",
    "operatorID":"0001",
    "requestType":1,
    "num":1
}

r_headers = {"Content-type": "application/json"}

r = requests.post('http://127.0.0.1', json=r_json, headers=r_headers)
print(r.status_code)
print(r.json())