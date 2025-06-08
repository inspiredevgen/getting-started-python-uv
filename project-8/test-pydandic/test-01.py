from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_is_odd():
    response = client.get("/is_odd?number=3")
    assert response.status_code == 200
    assert response.json() == {"result": "3 is odd"}

    response = client.get("/is_odd?number=4")
    assert response.status_code == 200
    assert response.json() == {"result": "4 is not odd"}

def test_is_odd_number():
    response = client.get("/is_odd/5")
    assert response.status_code == 200
    assert response.json() == {"result": "5 is odd"}

    response = client.get("/is_odd/6")
    assert response.status_code == 200
    assert response.json() == {"result": "6 is not odd"}

def test_create_item():
    item_data = {
        "name": "Test Item",
        "description": "This is a test item",
        "price": 10.99,
        "in_stock": True
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == {"message": f"Item {item_data} was created successfully"}

def test_create_item_without_description():
    item_data = {
        "name": "Test Item Without Description",
        "price": 15.99,
        "in_stock": False
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == {"message": f"Item {item_data} was created successfully"}
def test_create_item_without_in_stock():
    item_data = {
        "name": "Test Item Without In Stock",
        "description": "This item has no stock status",
        "price": 20.99
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == {"message": f"Item {item_data} was created successfully"}
def test_create_item_without_price():
    item_data = {
        "name": "Test Item Without Price",
        "description": "This item has no price",
        "in_stock": True
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 422  # Expecting validation error due to missing price
    assert "price" in response.json()["detail"][0]["loc"]
def test_create_item_with_invalid_price():
    item_data = {
        "name": "Test Item With Invalid Price",
        "description": "This item has an invalid price",
        "price": "not_a_number",  # Invalid price
        "in_stock": True
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 422  # Expecting validation error due to invalid price
    assert "price" in response.json()["detail"][0]["loc"]
def test_create_item_with_missing_name():
    item_data = {
        "description": "This item has no name",
        "price": 10.99,
        "in_stock": True
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 422  # Expecting validation error due to missing name
    assert "name" in response.json()["detail"][0]["loc"]
def test_create_item_with_empty_name():
    item_data = {
        "name": "",  # Empty name
        "description": "This item has an empty name",
        "price": 10.99,
        "in_stock": True
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 422  # Expecting validation error due to empty name
    assert "name" in response.json()["detail"][0]["loc"]
def test_create_item_with_special_characters_in_name():
    item_data = {
        "name": "Test Item @#&*",
        "description": "This item has special characters in the name",
        "price": 10.99,
        "in_stock": True
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200  # Assuming special characters are allowed
    assert response.json() == {"message": f"Item {item_data} was created successfully"}
def test_create_item_with_large_price():
    item_data = {
        "name": "Test Item with Large Price",
        "description": "This item has a very large price",
        "price": 1e6,  # Large price
        "in_stock": True
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200  # Assuming large prices are allowed
    assert response.json() == {"message": f"Item {item_data} was created successfully"}
def test_create_item_with_negative_price():
    item_data = {
        "name": "Test Item with Negative Price",
        "description": "This item has a negative price",
        "price": -10.99,  # Negative price
        "in_stock": True
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 422  # Expecting validation error due to negative price
    assert "price" in response.json()["detail"][0]["loc"]
def test_create_item_with_large_description():
    item_data = {
        "name": "Test Item with Large Description",
        "description": "x" * 1000,  # Very large description
        "price": 10.99,
        "in_stock": True
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200  # Assuming large descriptions are allowed
    assert response.json() == {"message": f"Item {item_data} was created successfully"}
