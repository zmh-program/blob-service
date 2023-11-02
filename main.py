from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from processor import process_file
from config import *


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
    return {
        "status": True,
        "project": "Chat Nio Blob Service",
        "description": "file processing and storage service",
        "service": SERVICE,
        "docs": EXPOSE + "/docs",
        "interface": EXPOSE + "/redoc",
        "repository": "https://github.com/Deeptrain-Community/chatnio-blob-service",
    }


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    """Accepts file and returns its contents."""

    try:
        contents = await process_file(file)
        return {
            "status": True,
            "content": contents,
            "error": "",
        }
    except Exception as e:
        return {
            "status": False,
            "content": "",
            "error": str(e),
        }
