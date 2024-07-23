from fastapi import UploadFile

from config import STORAGE_TYPE

from store.common import process_base64
from store.local import process_local
from store.s3 import process_s3
from store.telegram import process_tg

IMAGE_HANDLERS = {
    "common": process_base64,
    "local": process_local,
    "s3": process_s3,
    "tg": process_tg,
}


async def process_image(file: UploadFile) -> str:
    """Process image"""

    handler = IMAGE_HANDLERS.get(STORAGE_TYPE, IMAGE_HANDLERS["common"])
    return await handler(file)


async def process_all(file: UploadFile) -> str:
    """Process all files"""

    if STORAGE_TYPE == "common":
        raise ValueError("Cannot Use `Save All` Options Without Storage Config")

    return await process_image(file)
