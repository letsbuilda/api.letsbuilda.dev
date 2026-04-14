"""Test fixtures for the test suite."""

from typing import TYPE_CHECKING

import pytest
from litestar.testing import TestClient

from api.server import app

if TYPE_CHECKING:
    from collections.abc import Iterator

    from litestar import Litestar

app.debug = True


@pytest.fixture
def test_client() -> Iterator[TestClient[Litestar]]:
    """Create a test client for the Litestar app."""
    with TestClient(app=app) as client:
        yield client
