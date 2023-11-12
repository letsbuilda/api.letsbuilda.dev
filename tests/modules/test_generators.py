"""Test the generators module."""

import uuid
from http import HTTPStatus

from api.server import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_bulk_uuids() -> None:
    """Test bulk UUIDs."""
    response = client.post("/generators/uuids/", json={"uuid_type": 1, "quantity": 1})
    assert response.status_code == HTTPStatus.OK
    first = response.json()["uuids"][0]
    assert isinstance(uuid.UUID(first), uuid.UUID)


def test_random_numbers() -> None:
    """Test random numbers."""
    response = client.post("/generators/random-numbers/", json={})
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "numbers": [1],
        "total": 1,
    }
