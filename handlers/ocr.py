from fastapi import UploadFile, File
import requests
from config import OCR_ENDPOINT, OCR_SKIP_MODELS, OCR_SPEC_MODELS
import time
from typing import List

from utils import contains


def get_ocr_source(data: any) -> List[str]:
    if type(data) is str:
        return [data]
    elif type(data) is list:
        # recursive call and merge the results
        return sum([get_ocr_source(item) for item in data], [])

    return []


def create_ocr_task(file: UploadFile = File(...)) -> str:
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


def deprecated_could_enable_ocr(model: str = "") -> bool:
    if len(OCR_ENDPOINT) == 0:
        # if OCR is disabled
        return False

    if len(model) == 0:
        # if model is not defined
        return True

    if len(OCR_SPEC_MODELS) > 0:
        if contains(model, OCR_SPEC_MODELS):
            # if model is in specific list
            return True

    if contains(model, OCR_SKIP_MODELS):
        # if model is in skip list
        return False

    return True
