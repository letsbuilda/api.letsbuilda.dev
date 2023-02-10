from fastapi import APIRouter, FastAPI
from imsosorry import uwuify
from pydantic import BaseModel

from . import __version__

app = FastAPI(
    title="Let's Build A API",
    description="An API to host Let's Build A's projects",
    version=__version__,
)

router_root = APIRouter()


@router_root.get("/")
async def root():
    return {
        "message": "Hello World",
        "version": __version__,
    }


app.include_router(router_root)

router_fun = APIRouter(prefix="/fun", tags=["fun"])


class TextModel(BaseModel):
    text: str


@router_fun.post("/uwuify/")
async def uwuify_route(text: TextModel):
    return {"text": uwuify(text.text)}


app.include_router(router_fun)
