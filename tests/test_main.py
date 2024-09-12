import os
import pytest
from flask import Flask
from flask.testing import FlaskClient

# Import the Flask app from your application file
from main import app  

@pytest.fixture
def client() -> FlaskClient:
    with app.test_client() as client:
        yield client

def test_hello_world(client: FlaskClient):
    """Test the hello world endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "Hello PathwayTips!"

def test_pore_api_get(client: FlaskClient):
    """Test the PORE API GET endpoint"""
    response = client.get("/pore")
    assert response.status_code == 200
    assert response.json["message"] == "PORE API functionality is not yet available."

def test_pore_api_post(client: FlaskClient):
    """Test the PORE API POST endpoint"""
    response = client.post("/pore")
    assert response.status_code == 200
    assert response.json["message"] == "PORE API functionality (POST) is not yet implemented."
