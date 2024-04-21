from datetime import datetime

from fastapi import UploadFile

from config import LOCAL_STORAGE_DOMAIN
from util import md5_encode


async def process_local(file: UploadFile) -> str:
    """Process image and return its base64 url."""

    filename = md5_encode(file.filename + datetime.now().isoformat())
    path = f"static/{filename}"

    with open(path, "wb") as f:
        contents = await file.read()
        f.write(contents)

    return f"{LOCAL_STORAGE_DOMAIN}/{path}"
