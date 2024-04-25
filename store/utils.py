from datetime import datetime
from utils import md5_encode


def store_filename(filename: str) -> str:
    """Store filename."""
    suffix = filename.split(".")[-1] if "." in filename else "jpg"
    return md5_encode(filename + datetime.now().isoformat()) + "." + suffix
