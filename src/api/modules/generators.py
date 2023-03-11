"""Generation of things"""

import uuid
from typing import Literal

from fastapi import APIRouter

# pylint: disable-next=no-name-in-module
from pydantic import BaseModel, Field

router_generators = APIRouter(prefix="/generators", tags=["generators"])


class UUIDs(BaseModel):
    """Model to hold a list of UUIDs"""

    uuids: list[str]


class UUIDConfig(BaseModel):
    """Model to hold configuration for UUID generation"""

    uuid_type: Literal[1, 4]
    quantity: int = Field(gt=0, default=1)


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
