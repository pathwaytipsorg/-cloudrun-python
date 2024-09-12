# tests/test_main.py
import sys
import os

# Add the project directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from main import app


def test_homepage():
    # Create a test client using Flask's app
    client = app.test_client()

    # Send a request to the homepage
    response = client.get("/")

    # Assert the response is 200 (OK)
    assert response.status_code == 200

    # Check if the name in the response is correct
    assert b"Hello PathwayTips!" in response.data
