"""Generation of things"""

import uuid
from random import randint
from typing import Literal

from fastapi import APIRouter

# pylint: disable-next=no-name-in-module
from pydantic import BaseModel, Field, validator

router_generators = APIRouter(prefix="/generators", tags=["generators"])


class UUIDConfig(BaseModel):
    """Model to hold configuration for UUID generation"""

    uuid_type: Literal[1, 4]
    quantity: int = Field(gt=0, default=1)


class UUIDs(BaseModel):
    """Model to hold a list of UUIDs"""

    uuids: list[str]


@router_generators.post("/uuids/")
async def bulk_uuids(config: UUIDConfig) -> UUIDs:
    """Generate bulk UUIDs"""
    if config.uuid_type == 1:
        function = uuid.uuid1
    elif config.uuid_type == 4:
        function = uuid.uuid4
    else:
        raise ValueError(f"unsupported UUID type: {config.uuid_type}")
    uuids = [str(function()) for _ in range(config.quantity)]
    return UUIDs(uuids=uuids)


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


@router_generators.post("/random-numbers/")
async def random_numbers(config: NumbersConfig) -> Numbers:
    """Generate bulk random numbers"""
    numbers = [randint(config.lower_bound, config.upper_bound) for _ in range(config.quantity)]
    return Numbers(numbers=numbers, total=sum(numbers))
