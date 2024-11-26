import json
import pytest
from Exercises.Exercise_3.Exercise3 import gbp_to_target

@pytest.fixture
def sample_data():
    return {
        "rates": {
            "USD": 1.25,
            "GBP": 1.0,
            "EUR": 1.15,
            "JPY": 150.0,
            "CNY": 8.2,
            "BRL": 5.0,
            "SAR": 4.8
        }
    }

def test_currency_conversion(sample_data, monkeypatch):
    def mock_load(file):
        return sample_data
    monkeypatch.setattr(json, "load", mock_load)
    result = gbp_to_target(100)
    assert result["USD"] == 125.0, "Conversion to USD is incorrect."
    assert result["EUR"] == 115.0, "Conversion to EUR is incorrect."
