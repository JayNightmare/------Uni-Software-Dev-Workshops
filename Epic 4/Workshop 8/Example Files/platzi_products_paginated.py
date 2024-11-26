import requests
import json

BASE_URL = 'https://api.escuelajs.co/api/v1/products/'

def get_products(offset=0, limit=10):
    while True:
        try:
            response = requests.get(BASE_URL, params={
                'offset': offset,
                'limit': limit
            })
            response.raise_for_status()
            data = response.json()

            for product in data:
                id = product["id"]
                price = product["price"]
                category_name = product["category"]["name"]
                print(f"Product id: {id}, price: {price}, category: {category_name}")

            # Check if there are more products to fetch
            if len(data) < limit:
                break
            
            # Update offset for the next iteration
            offset += limit
            username = input("Hit Enter, or q to quit")
            if username == "q":
                break
        # In case the request times out
        except requests.exceptions.Timeout as err:
            print(f"Timeout error occurred: {err}")
        # In case the HTTP request fails
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        # In case the JSON decoding fails
        except json.JSONDecodeError as err:
            print(f"JSON decoding error occurred: {err}")

get_products()