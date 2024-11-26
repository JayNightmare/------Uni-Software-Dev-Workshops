import csv
import requests
import os

API_URL = 'https://api.escuelajs.co/api/v1/products/'

def create_products_from_csv(csv_file):
    # Check if the CSV file exists
    if not os.path.exists(csv_file):
        print(f"CSV file '{csv_file}' not found. Creating a new one...")
        # Create the file with a predefined structure
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Header
            writer.writerow(['title', 'price', 'description', 'categoryId', 'image'])
            # Example row
            writer.writerow(['Example Product', 10, 'Example Description', 1, 'https://placeimg.com/640/480/any'])
        print(f"Template CSV file '{csv_file}' created. Please fill it with product data and rerun the script.")
        return

    # Process the CSV file if it exists
    try:
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                new_product = {
                    "title": row['title'],
                    "price": int(row['price']),
                    "description": row['description'],
                    "categoryId": int(row['categoryId']),
                    "images": [row['image']]
                }
                try:
                    response = requests.post(API_URL, json=new_product)
                    response.raise_for_status()
                    print(f"Created Product: {new_product['title']}, Status: {response.status_code}")
                except requests.exceptions.RequestException as err:
                    print(f"Failed to create product {new_product['title']}: {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

create_products_from_csv('Epic 4/Workshop 8/Excersies/Exercise 1/products.csv')
