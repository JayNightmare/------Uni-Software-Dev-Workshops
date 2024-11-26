from unittest.mock import patch
from Exercises.Exercise_2.Exercise2 import can_catch_bus

@patch("Exercise2.Exercise2.requests.get")
def test_can_catch_bus(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {"lineId": "57", "timeToStation": 300},  # 5 minutes
        {"lineId": "57", "timeToStation": 900}   # 15 minutes
    ]
    can_catch_bus(12)
    assert mock_get.called, "API call for TFL was not made."
