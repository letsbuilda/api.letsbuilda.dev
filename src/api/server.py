"""API server definition"""

from os import getenv
from random import randint

import sentry_sdk
from fastapi import APIRouter, FastAPI
from imsosorry import uwuify

# pylint: disable-next=no-name-in-module
from pydantic import BaseModel

from . import __version__
from .modules.generators import router_generators

release_prefix = getenv("API_SENTRY_RELEASE_PREFIX", "api")
git_sha = getenv("GIT_SHA", "development")
sentry_sdk.init(
    dsn=getenv("API_SENTRY_DSN"),
    environment=getenv("API_SENTRY_ENV"),
    send_default_pii=True,
    traces_sample_rate=1.0,
    _experiments={
        "profiles_sample_rate": 1.0,
    },
    release=f"{release_prefix}@{git_sha}",
)


class TextModel(BaseModel):
    """Generic model for accepting arbitrary plain-text input"""

    text: str


class Numbers(BaseModel):
    """Model to hold a list of numbers"""

    numbers: list[int]
    total: int


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


@router_fun.get("/random-numbers/{quantity}/{range_high}")
async def random_numbers(quantity: int, range_high: int) -> Numbers:
    """Generate bulk random numbers"""
    numbers = [randint(1, range_high) for _ in range(quantity)]
    return Numbers(numbers=numbers, total=sum(numbers))


app.include_router(router_fun)

app.include_router(router_generators)
