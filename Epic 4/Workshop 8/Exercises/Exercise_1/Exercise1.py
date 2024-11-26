import requests

API_URL = 'https://api.escuelajs.co/api/v1/products/'

# ? Step 1: View a specific product
def view_product(product_id):
    try:
        response = requests.get(API_URL + str(product_id))
        response.raise_for_status()
        product = response.json()
        print(f"Product ID: {product['id']}\nTitle: {product['title']}\nPrice: {product['price']}\nCategory: {product['category']['name']}")
    
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.Timeout as err:
        print(f"Timeout error occurred: {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
        
# ? Step 2: Filter products by price
def filter_by_price(max_price):
    try:
        response = requests.get(API_URL, params={"limit": 5})
        response.raise_for_status()
        products = response.json()
        filtered = [p for p in products if p['price'] <= max_price]
        print(f"\n\nProducts under ${max_price}: {[p['title'] for p in filtered]}")
        return filtered
    
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.Timeout as err:
        print(f"Timeout error occurred: {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

# ? Step 3: Filter products by category
def filter_by_category(category_name):
    try: 
        response = requests.get(API_URL, params={"limit": 5})
        response.raise_for_status()
        products = response.json()
        filtered = [p for p in products if p['category']['name'].lower() == category_name.lower()]
        print(f"\n\nProducts in category '{category_name}': {[p['title'] for p in filtered]}")
        return filtered
    
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.Timeout as err:
        print(f"Timeout error occurred: {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

# ? Step 4: Combine filters
def filter_by_price_and_category(max_price, category_name):
    filtered_price = filter_by_price(max_price)
    filtered_combined = [p for p in filtered_price if p['category']['name'].lower() == category_name.lower()]
    print(f"\n\nProducts in category '{category_name}' under ${max_price}: {[p['title'] for p in filtered_combined]}")

# ! Execution
view_product(140)  # * View product with ID 14
filter_by_price(10)  # * Products under $10
filter_by_category('Clothes')  # * Products in the category "Clothes"
filter_by_price_and_category(10, 'Clothes')  # * Combined filter
