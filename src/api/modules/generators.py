"""Generation of things."""

import uuid
from random import randint
from typing import Literal

from litestar import Controller, post
from pydantic import BaseModel, Field, validator


class UUIDConfig(BaseModel):
    """Model to hold datauration for UUID generation."""

    uuid_type: Literal[1, 4]
    quantity: int = Field(gt=0, default=1)


class UUIDs(BaseModel):
    """Model to hold a list of UUIDs."""

    uuids: list[str]


class NumbersConfig(BaseModel):
    """Model to hold datauration for number generation."""

    lower_bound: int = Field(default=1)
    upper_bound: int = Field(default=1)
    quantity: int = Field(gt=0, default=1)

    @validator("upper_bound")
    def upper_bound_must_be_greater_than_lower_bound(cls, v: int, values: dict) -> int:  # type: ignore[type-arg] # noqa: N805
        """Confirm upper bound is greater than lower bound."""
        if "lower_bound" in values and v < values["lower_bound"]:
            msg = "upper bound must be greater than lower bound"
            raise ValueError(msg)
        return v


class Numbers(BaseModel):
    """Model to hold a list of numbers."""

    numbers: list[int]
    total: int


class GeneratorController(Controller):
    """Generator controller."""

    path = "/generators"

    @post("/random-numbers/", status_code=200)
    async def random_numbers(self, data: NumbersConfig) -> Numbers:
        """Generate bulk random numbers."""
        numbers = [randint(data.lower_bound, data.upper_bound) for _ in range(data.quantity)]
        return Numbers(numbers=numbers, total=sum(numbers))

    @post("/uuids/", status_code=200)
    async def bulk_uuids(self, data: UUIDConfig) -> UUIDs:
        """Generate bulk UUIDs."""
        if data.uuid_type == 1:
            function = uuid.uuid1
        elif data.uuid_type == 4:  # noqa: PLR2004 - comparing ints
            function = uuid.uuid4
        else:
            msg = f"unsupported UUID type: {data.uuid_type}"
            raise ValueError(msg)
        uuids = [str(function()) for _ in range(data.quantity)]
        return UUIDs(uuids=uuids)
