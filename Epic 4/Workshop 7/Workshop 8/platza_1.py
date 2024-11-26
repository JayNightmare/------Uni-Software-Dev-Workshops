import requests
import json

API_URL = 'https://api.escuelajs.co/api/v1/products/'

try:
    response = requests.get(API_URL + '14')
    response.raise_for_status()
    data = response.json()
    id = data["id"]
    price = data["price"]
    category_name = data["category"]["name"]
    print(f"Product id: {id}, price: {price}, category: {category_name}")

# In case the request times out
except requests.exceptions.Timeout as err:
    print(f"Timeout error occurred: {err}")
# In case the HTTP request fails
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
# In case the JSON decoding fails
except json.JSONDecodeError as err:
    print(f"JSON decoding error occurred: {err}")
# In case the "thumbnailUrl" key or the data structure is missing    
except KeyError as err:
    print(f"KeyError occurred: {err}")
# In case there are not enough items in the data list
except IndexError as err:
    print(f"IndexError occurred: {err}")
# An except Exception block is added to catch unexpected errors that might occur during the execution of the code. This is a catch-all block that will catch any error that is not handled by the previous except blocks. This is useful for debugging purposes, but it is not recommended to use this block in production code.
except Exception as err:
    print(f"An unexpected error occurred: {err}")
