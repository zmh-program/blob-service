from fastapi import UploadFile

from config import STORAGE_TYPE

from store.common import process_base64
from store.local import process_local

IMAGE_HANDLERS = {
    "common": process_base64,
    "local": process_local,
}


async def process_image(file: UploadFile) -> str:
    """Process image"""

    handler = IMAGE_HANDLERS.get(STORAGE_TYPE, IMAGE_HANDLERS["common"])
    return await handler(file)
