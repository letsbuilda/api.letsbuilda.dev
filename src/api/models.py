"""Model definitions"""

from pydantic import BaseModel
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


class TextModel(BaseModel):
    """Generic model for accepting arbitrary plain-text input"""

    text: str
