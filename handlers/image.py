import time
from fastapi import UploadFile
from config import EXPOSE

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


def save_image(file: UploadFile) -> str:
    """Saves image to path."""
    name, suffix = file.filename.split(".")
    path = f"static/{name}_{int(time.time())}.{suffix}"

    with open(path, "wb") as buffer:
        buffer.write(file.file.read())

    return path


def process(file: UploadFile) -> str:
    """Process image and return its url."""
    path = save_image(file)
    return f"{EXPOSE}/{path}"
