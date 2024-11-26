import requests
import json

try:
    response = requests.get('https://jsonplaceholder.typicode.com/photos')
    response.raise_for_status()
    data = response.json()
    thumbnail_urls = data[3]['thumbnailUrl']
    print(thumbnail_urls)
    
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except json.JSONDecodeError as e:
    print(f"JSON Decode Error: {e}")
except KeyError as e:
    print(f"Key Error: {e}")
except IndexError as e:
    print(f"Index Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")