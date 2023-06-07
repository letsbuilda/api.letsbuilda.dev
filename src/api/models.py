"""Model definitions"""

from typing import Literal

from pydantic import BaseModel, Field, validator
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


class UUIDConfig(BaseModel):
    """Model to hold configuration for UUID generation"""

    uuid_type: Literal[1, 4]
    quantity: int = Field(gt=0, default=1)


class UUIDs(BaseModel):
    """Model to hold a list of UUIDs"""

    uuids: list[str]


class NumbersConfig(BaseModel):
    """Model to hold configuration for number generation"""

    lower_bound: int = Field(default=1)
    upper_bound: int = Field(default=1)
    quantity: int = Field(gt=0, default=1)

    @validator("upper_bound")
    def upper_bound_must_be_greater_than_lower_bound(cls, v, values):
        """Confirm upper bound is greater than lower bound"""
        if "lower_bound" in values and v < values["lower_bound"]:
            raise ValueError("upper bound must be greater than lower bound")
        return v


class Numbers(BaseModel):
    """Model to hold a list of numbers"""

    numbers: list[int]
    total: int
