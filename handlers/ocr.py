from fastapi import UploadFile, File
import requests
from config import OCR_ENDPOINT
import time


def get_ocr_source(data: any) -> list:
    if type(data) is str:
        return [data]
    elif type(data) is list:
        # recursive call and merge the results
        return sum([get_ocr_source(item) for item in data], [])

    return []


def ocr_image(file: UploadFile = File(...)) -> str:
    start = time.time()

    response = requests.post(
        OCR_ENDPOINT + "/ocr/predict-by-file",
        files={"file": (file.filename, file.file, file.content_type)},
    )
    response.raise_for_status()
    data = response.json()

    code = data.get("resultcode", -1)
    message = data.get("message", "")
    result = data.get("data", [])

    if code != 200:
        raise ValueError(f"OCR API error: {message} (code: {code})")

    print(f"[orc] time taken: {time.time() - start:.2f}s (file: {file.filename})")

    return " ".join(get_ocr_source(result))
