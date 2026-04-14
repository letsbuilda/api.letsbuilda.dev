"""Test server."""

from http import HTTPStatus
from typing import TYPE_CHECKING

from api import __version__

if TYPE_CHECKING:
    from litestar import Litestar
    from litestar.testing import TestClient


def test_get_metadata(test_client: TestClient[Litestar]) -> None:
    """Test getting the root route."""
    response = test_client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "version": __version__,
        "server_commit": "development",
    }
