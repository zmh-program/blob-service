from fastapi import UploadFile
from store.store import process_image

COMMON_IMAGE_EXTENSIONS = {
    "png", "jpg", "jpeg", "gif", "bmp", "svg", "webp",
    "tiff", "tif", "psd", "raw", "heif", "indd",
    "jp2", "j2k", "jpf", "jpx", "jpm", "mj2",
    "ico", "cur", "ani", "apng", "cur", "ani", "apng",
    "ps", "eps", "ai", "psb", "tif", "tiff", "svgz",
    "dwg", "dxf", "gpx", "kml", "kmz", "3ds", "c4d",
}


def is_image(filename: str) -> bool:
    """Returns True if filename is an image."""
    return filename.split(".")[-1] in COMMON_IMAGE_EXTENSIONS


async def process(file: UploadFile) -> str:
    """Process image."""

    return await process_image(file)
