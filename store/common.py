import base64
from fastapi import UploadFile


async def process_base64(file: UploadFile) -> str:
    """Process image and return its base64 url."""

    contents = await file.read()
    encoded = base64.b64encode(contents).decode("utf-8")
    return f"data:{file.content_type};base64,{encoded}"
