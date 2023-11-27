from fastapi import UploadFile, File

from config import ENABLE_AZURE_SPEECH
from handlers import (
    pdf,
    word,
    ppt,
    xlsx,
    image,
    speech,
)


async def process_file(file: UploadFile = File(...)) -> str:
    """Process file and return its contents."""
    filename = file.filename.lower()
    if pdf.is_pdf(filename):
        return pdf.process(file)
    elif word.is_docx(filename):
        return word.process(file)
    elif ppt.is_pptx(filename):
        return ppt.process(file)
    elif xlsx.is_xlsx(filename):
        return xlsx.process(file)
    elif image.is_image(filename):
        return image.process(file)
    elif ENABLE_AZURE_SPEECH and speech.is_audio(filename):
        return speech.process(file)

    content = await file.read()
    return content.decode("utf-8")
