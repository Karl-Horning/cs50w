import requests

res = requests.get('http://127.0.0.1:5000/api/flights/1')
data = res.json()

print(data['passengers'])