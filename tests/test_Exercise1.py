from unittest.mock import patch
from Excersies.Exercise_1.Exercise1 import view_product, filter_by_price, filter_by_category

@patch("Exercise1.Exercise1.requests.get")
def test_view_product(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "id": 14, "title": "Test Product", "price": 10, "category": {"name": "Test Category"}
    }
    view_product(14)
    assert mock_get.called, "API call for viewing product was not made."

@patch("Exercise1.Exercise1.requests.get")
def test_filter_by_price(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {"price": 5, "title": "Cheap Product"},
        {"price": 15, "title": "Expensive Product"}
    ]
    result = filter_by_price(10)
    assert len(result) == 1, "Filter by price did not return correct results."

@patch("Exercise1.Exercise1.requests.get")
def test_filter_by_category(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {"category": {"name": "Clothes"}, "title": "T-Shirt"},
        {"category": {"name": "Electronics"}, "title": "Laptop"}
    ]
    result = filter_by_category("Clothes")
    assert len(result) == 1, "Filter by category did not return correct results."
