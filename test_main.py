# test_main.py
import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_cities_of_spain():
    response = client.get('/countries/Spain')
    assert response.status_code == 200
    expected_cities = ["Seville", "Madrid", "Barcelona"]  # Replace with all actual cities from your data
    assert set(response.json()) == set(expected_cities)