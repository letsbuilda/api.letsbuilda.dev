"""Test fixtures for the test suite."""

from collections.abc import Iterator

import pytest
from litestar import Litestar
from litestar.testing import TestClient

from api.server import app

app.debug = True


@pytest.fixture
def test_client() -> Iterator[TestClient[Litestar]]:
    """Create a test client for the Litestar app."""
    with TestClient(app=app) as client:
        yield client
