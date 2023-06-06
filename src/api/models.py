"""Model definitions"""

from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class Error:
    """Returned when an error occurs"""

    detail: str


@dataclass(frozen=True)
class ServerMetadata:
    """Metadata about the server"""

    version: str
    server_commit: str
