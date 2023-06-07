"""Generation of things"""

import uuid
from random import randint

from fastapi import APIRouter

from api.models import Numbers, NumbersConfig, UUIDConfig, UUIDs

router = APIRouter(prefix="/generators", tags=["generators"])


@router.post("/uuids/")
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


@router.post("/random-numbers/")
async def random_numbers(config: NumbersConfig) -> Numbers:
    """Generate bulk random numbers"""
    numbers = [randint(config.lower_bound, config.upper_bound) for _ in range(config.quantity)]
    return Numbers(numbers=numbers, total=sum(numbers))
