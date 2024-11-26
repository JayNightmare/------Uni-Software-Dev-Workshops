import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")

if response.status_code == 200:
    data = json.loads(response.text)
    print(data[:3])