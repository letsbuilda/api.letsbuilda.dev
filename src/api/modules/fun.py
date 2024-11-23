"""Fun module for API."""

from imsosorry import uwuify
from litestar import Controller, post

from api.models import TextModel


class FunController(Controller):
    """Fun controller."""

    path = "/fun"

    @post("/uwuify/", status_code=200)
    async def uwuify(self, data: TextModel) -> dict[str, str]:
        """UwUify text."""
        return {"text": uwuify(data.text)}
