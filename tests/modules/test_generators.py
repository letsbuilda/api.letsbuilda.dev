"""Test the generators module"""

import uuid

from fastapi.testclient import TestClient

from api.server import app

client = TestClient(app)


def test_bulk_uuids():
    response = client.post("/generators/uuids/", json={"uuid_type": 1, "quantity": 1})
    assert response.status_code == 200
    first = response.json()["uuids"][0]
    assert isinstance(uuid.UUID(first), uuid.UUID)


def test_random_numbers():
    response = client.post("/generators/random-numbers/", json={})
    assert response.status_code == 200
    assert response.json() == {
        "numbers": [1],
        "total": 1,
    }
