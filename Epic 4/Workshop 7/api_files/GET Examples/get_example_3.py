import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

try:
    response.raise_for_status()
    data = response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except json.JSONDecodeError as e:
    print(f"JSON Decode Error: {e}")
print(data[:5])