from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from handlers.processor import process_file
from config import *
from handlers.ocr import create_ocr_task, deprecated_could_enable_ocr

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOW_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return FileResponse("index.html", media_type="text/html")


@app.get("/favicon.ico")
def favicon():
    return FileResponse("favicon.ico")


@app.post("/upload")
async def upload(
        file: UploadFile = File(...),
        enable_ocr: bool = Form(default=False),
        enable_vision: bool = Form(default=True),
        save_all: bool = Form(default=False),
        model: str = Form(default=""),  # deprecated
):
    """Accepts file and returns its contents."""

    if model and len(model) > 0:
        # compatibility with deprecated model parameter
        enable_ocr = deprecated_could_enable_ocr(model)
        enable_vision = not enable_ocr

    if len(OCR_ENDPOINT) == 0:
        enable_ocr = False

    try:
        filetype, contents = await process_file(
            file,
            enable_ocr=enable_ocr,
            enable_vision=enable_vision,
            save_all=save_all,
        )
        return {
            "status": True,
            "content": contents,
            "type": filetype,
            "error": "",
        }
    except Exception as e:
        return {
            "status": False,
            "content": "",
            "type": "error",
            "error": str(e),
        }
