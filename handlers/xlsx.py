from io import BytesIO
from fastapi import UploadFile
import openpyxl
import xlrd


def is_xlsx(filename: str) -> bool:
    """Return True if file is xlsx."""
    return filename.endswith(".xlsx") or filename.endswith(".xls")


def process(file: UploadFile) -> str:
    """
    Process xlsx file and return its contents along with hyperlinks.
    Format:
      - URL: [content](url)
    """
    if file.filename.endswith(".xlsx"):
        content = file.file.read()
        wb = openpyxl.load_workbook(BytesIO(content), data_only=True)
        sheet = wb.active
        rows = []
        for row in sheet.iter_rows():
            row_data = []
            for cell in row:
                if cell.hyperlink:
                    cell_value = f"[{cell.value}]({cell.hyperlink.target})"
                else:
                    cell_value = cell.value
                if cell_value:
                    row_data.append(str(cell_value))
            if row_data:
                rows.append("\t".join(row_data))
        return "\n".join(rows)
    else:
        # Assuming no need for hyperlink extraction in other file formats
        content = file.file.read()
        wb = xlrd.open_workbook(file_contents=content)
        sheet = wb.sheet_by_index(0)
        return "\n".join(
            "\t".join(str(cell.value) for cell in row if cell.value)
            for row in sheet.get_rows() if any(cell.value for cell in row)
        )
