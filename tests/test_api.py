from unittest.mock import patch
from lib.api import fetch_product


@patch("lib.api.requests.get")
def test_fetch_product_success(mock_get):
    mock_get.return_value.json.return_value = {
        "product": {
            "product_name": "Chocolate",
            "brands": "Oreo",
            "ingredients_text": "Cocoa, sugar, flour"
        }
    }

    result = fetch_product("123456789")

    assert result["name"] == "Chocolate"
    assert result["brand"] == "Oreo"
    assert result["barcode"] == "123456789"


@patch("lib.api.requests.get")
def test_fetch_product_not_found(mock_get):
    mock_get.return_value.json.return_value = {}

    result = fetch_product("987654321")

    assert result is None