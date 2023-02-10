"""API server definition"""

from fastapi import APIRouter, FastAPI
from imsosorry import uwuify

# pylint: disable-next=no-name-in-module
from pydantic import BaseModel

from . import __version__


class TextModel(BaseModel):
    """Generic model for accepting arbitrary plain-text input"""

    text: str


app = FastAPI(
    title="Let's Build A API",
    description="An API to host Let's Build A's projects",
    version=__version__,
)

router_root = APIRouter()


@router_root.get("/")
async def root_route():
    """Get base metadata"""
    return {
        "message": "Welcome to the API",
        "version": __version__,
    }


app.include_router(router_root)

router_fun = APIRouter(prefix="/fun", tags=["fun"])


@router_fun.post("/uwuify/")
async def uwuify_route(text: TextModel):
    """Convert text to UwU meme style"""
    return {"text": uwuify(text.text)}


app.include_router(router_fun)
