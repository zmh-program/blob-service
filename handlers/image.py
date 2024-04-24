from fastapi import UploadFile
from handlers.ocr import ocr_image, could_enable_ocr
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


async def process(file: UploadFile, model: str) -> str:
    """Process image."""
    if could_enable_ocr(model):
        return ocr_image(file)

    return await process_image(file)
