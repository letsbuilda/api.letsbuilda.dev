"""Test server."""

from http import HTTPStatus

from api import __version__
from api.server import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main() -> None:
    """Test getting the root route."""
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "version": __version__,
        "server_commit": "development",
    }
