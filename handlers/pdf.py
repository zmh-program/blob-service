from io import BytesIO

from fastapi import UploadFile
import fitz

from config import PDF_MAX_IMAGES
from handlers.image import process as process_image


def is_pdf(filename: str) -> bool:
    """Check if file is PDF."""
    return filename.endswith(".pdf")


async def process(file: UploadFile, enable_ocr: bool, enable_vision: bool) -> str:
    filename = file.filename.replace(" ", "_").replace(".", "_")
    doc = fitz.open("pdf", file.file.read())  # read the file from memory
    stack = []
    cursor = 0

    for page in doc:
        text = page.get_text()
        stack.append(text)

        if cursor >= PDF_MAX_IMAGES:
            # skip image extraction if images is full
            if PDF_MAX_IMAGES != -1:
                continue

        for image_instance in page.get_images(full=True):  # get all images on the page
            cursor += 1

            xref = image_instance[0]  # get the xref of the image
            image = doc.extract_image(xref)  # extract the image
            data = image['image']  # get the image data
            suffix = image.get('ext', '')  # get the image extension
            image_name = f"{filename}_extracted_{cursor}.{suffix}"  # create a name for the image
            io = BytesIO(data)
            io.name = image_name
            io.seek(0)

            # create a file-like object for the image
            image_file = UploadFile(io, filename=image_name)
            stack.append(await process_image(image_file, enable_ocr=enable_ocr, enable_vision=enable_vision, not_raise=True))

            print(f"[pdf] extracted image: {image_name} (page: {page.number}, cursor: {cursor}, max: {PDF_MAX_IMAGES})")

            if PDF_MAX_IMAGES != -1 and cursor >= PDF_MAX_IMAGES:
                break

    return "\n".join(stack)
