from io import BytesIO
from fastapi import UploadFile
from docx import Document


def is_docx(filename: str) -> bool:
    """Return True if filename is docx."""
    return filename.endswith(".docx") or filename.endswith(".doc")


def process(file: UploadFile) -> str:
    """Process docx file and return its contents."""
    content = file.file.read()
    doc = Document(BytesIO(content))
    return "\n".join([p.text for p in doc.paragraphs])
