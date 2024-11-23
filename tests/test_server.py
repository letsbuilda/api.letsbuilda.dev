"""Test server."""

from http import HTTPStatus

from litestar import Litestar
from litestar.testing import TestClient

from api import __version__


def test_get_metadata(test_client: TestClient[Litestar]) -> None:
    """Test getting the root route."""
    response = test_client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "version": __version__,
        "server_commit": "development",
    }
