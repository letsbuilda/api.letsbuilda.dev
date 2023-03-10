"""Test server"""

from fastapi.testclient import TestClient

from api import __version__
from api.server import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the API",
        "version": __version__,
    }


def test_read_random_numbers():
    response = client.get("/fun/random-numbers/1/1")
    assert response.status_code == 200
    assert response.json() == {
        "numbers": [1],
        "total": 1,
    }
