"""Test server"""

from fastapi.testclient import TestClient

from api import __version__
from api.server import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello World",
        "version": __version__,
    }
