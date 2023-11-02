import fastapi
import pypdf


def is_pdf(filename: str) -> bool:
    """Check if file is PDF."""
    return filename.endswith(".pdf")


def process(file: fastapi.File) -> str:
    reader = pypdf.PdfReader(file.file)
    return "\n".join([i.extract_text() for i in reader.pages])
