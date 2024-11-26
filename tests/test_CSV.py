import os
import csv
import pytest
from unittest.mock import patch
from Exercises.Exercise_1.CSV import create_products_from_csv

def test_create_csv_file():
    test_csv = "test_products.csv"
    if os.path.exists(test_csv):
        os.remove(test_csv)

    create_products_from_csv(test_csv)
    assert os.path.exists(test_csv), "CSV file was not created."

    with open(test_csv, newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows[0] == ['title', 'price', 'description', 'categoryId', 'image'], "CSV header is incorrect."
        assert len(rows) == 2, "Example row was not added to the CSV."

    os.remove(test_csv)

@patch("Exercise1.CSV.requests.post")
def test_post_api_request(mock_post):
    mock_post.return_value.status_code = 201
    create_products_from_csv("products.csv")
    assert mock_post.called, "API call was not made."
