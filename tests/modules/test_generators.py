"""Test the generators module."""

import uuid
from http import HTTPStatus

from litestar import Litestar
from litestar.testing import TestClient


def test_bulk_uuids(test_client: TestClient[Litestar]) -> None:
    """Test bulk UUIDs."""
    response = test_client.post("/generators/uuids/", json={"uuid_type": 1, "quantity": 1})
    assert response.status_code == HTTPStatus.OK
    first = response.json()["uuids"][0]
    assert isinstance(uuid.UUID(first), uuid.UUID)


def test_random_numbers(test_client: TestClient[Litestar]) -> None:
    """Test random numbers."""
    response = test_client.post("/generators/random-numbers/", json={})
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "numbers": [1],
        "total": 1,
    }
