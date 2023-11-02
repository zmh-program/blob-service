from io import BytesIO
from fastapi import UploadFile
import openpyxl


def is_xlsx(filename: str) -> bool:
    """Return True if file is xlsx."""
    return filename.endswith(".xlsx") or filename.endswith(".xls")


def process(file: UploadFile) -> str:
    """Process xlsx file and return its contents."""
    content = file.file.read()
    wb = openpyxl.load_workbook(BytesIO(content))
    sheet = wb.active
    return "\n".join(
        "\t".join(str(cell.value) for cell in row if cell.value)
        for row in sheet.rows if any(cell.value for cell in row)
    )
