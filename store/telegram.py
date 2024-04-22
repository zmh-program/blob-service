from fastapi import UploadFile
import requests
from config import TG_API


async def process_tg(file: UploadFile) -> str:
    """Process image and return its telegram url."""
    response = requests.post(
        TG_API,
        files={"image": (file.filename, file.file, file.content_type)},
    )
    response.raise_for_status()

    data = response.json()
    url = data.get("url")
    if not url:
        raise ValueError(f"Telegram API error: {data}")

    return url
