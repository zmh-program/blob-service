from fastapi import UploadFile, File

from config import ENABLE_AZURE_SPEECH, MAX_FILE_SIZE
from handlers import (
    pdf,
    word,
    ppt,
    xlsx,
    image,
    speech,
)


async def read_file_size(file: UploadFile) -> float:
    """Read file size and return it in MiB."""

    # dont using file.read() directly because it will consume the file content
    file_size = 0
    while chunk := await file.read(20480):  # read chunk of 20KiB per iteration
        file_size += len(chunk)
    await file.seek(0)
    return file_size / 1024 / 1024


async def process_file(file: UploadFile = File(...), model: str = "") -> str:
    """Process file and return its contents."""

    if MAX_FILE_SIZE > 0:
        file_size = await read_file_size(file)
        if file_size > MAX_FILE_SIZE:
            raise ValueError(f"File size {file_size:.2f} MiB exceeds the limit of {MAX_FILE_SIZE} MiB.")

    filename = file.filename.lower()
    if pdf.is_pdf(filename):
        return await pdf.process(file)
    elif word.is_docx(filename):
        return word.process(file)
    elif ppt.is_pptx(filename):
        return ppt.process(file)
    elif xlsx.is_xlsx(filename):
        return xlsx.process(file)
    elif image.is_image(filename):
        return await image.process(file, model)
    elif ENABLE_AZURE_SPEECH and speech.is_audio(filename):
        return speech.process(file)

    content = await file.read()
    return content.decode("utf-8")
