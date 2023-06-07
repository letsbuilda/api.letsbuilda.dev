from os import getenv

from fastapi import APIRouter

from api import __version__
from api.models import ServerMetadata

router = APIRouter(tags=["metadata"])


@router.get("/")
async def metadata() -> ServerMetadata:
    """Get server metadata"""
    return ServerMetadata(
        version=__version__,
        server_commit=getenv("GIT_SHA", "development"),
    )
