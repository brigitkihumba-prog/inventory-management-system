import pytest
from server.app import app, inventory

@pytest.fixture
def client():
    inventory.clear()
    inventory.extend([
        {
            "id": 1,
            "name": "Coca-Cola",
            "brand": "Coca-Cola",
            "price": 100,
            "stock": 10,
            "barcode": "123456789",
            "ingredients": "Carbonated water, sugar, flavouring"
        },
    ])
    app.config['TESTING'] = True
    return app.test_client()

def test_view_inventory(client):
    response = client.get("/inventory")
    assert response.status_code == 200

def test_view_product(client):
    response = client.get("/inventory/1")
    assert response.status_code == 200

def test_add_product(client):
    response = client.post("/inventory", json={
        "name": "Pepsi",
        "brand": "Pepsi",
        "price": 90,
        "stock": 5,
        "barcode": "987654321",
        "ingredients": "Carbonated water, sugar, flavouring"
    })
    assert response.status_code == 201

def test_update_product(client):
    response = client.put("/inventory/1", json={
        "price": 110,
    })
    assert response.status_code == 200  

def test_delete_product(client):
    response = client.delete("/inventory/1")
    assert response.status_code == 200

def test_product_not_found(client):
    response = client.get("/inventory/99")
    assert response.status_code == 404                  