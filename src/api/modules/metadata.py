"""Metadata module."""

from os import getenv

from litestar import Controller, get
from pydantic import BaseModel

from api import __version__


class ServerMetadata(BaseModel):
    """Metadata about the server."""

    version: str
    server_commit: str


class MetadataController(Controller):
    """Metadata controller."""

    path = "/"

    @get("/")
    async def server_metadata(self) -> ServerMetadata:
        """Return metadata about the server."""
        return ServerMetadata(
            version=__version__,
            server_commit=getenv("GIT_SHA", "development"),
        )
