from fastapi import APIRouter
from imsosorry import uwuify

from api.models import TextModel

router = APIRouter(prefix="/fun", tags=["fun"])


@router.post("/uwuify/")
async def uwuify_route(text: TextModel):
    """Convert text to UwU meme style"""
    return {"text": uwuify(text.text)}
