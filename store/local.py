from fastapi import UploadFile
from config import LOCAL_STORAGE_DOMAIN
from store.utils import store_filename


async def process_local(file: UploadFile) -> str:
    """Process image and return its direct url."""

    filename = store_filename(file.filename)
    path = f"static/{filename}"

    with open(path, "wb") as f:
        contents = await file.read()
        f.write(contents)

    return f"{LOCAL_STORAGE_DOMAIN}/{path}"
