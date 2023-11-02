from fastapi import UploadFile
from azure.cognitiveservices.speech import *
from config import (
    AZURE_SPEECH_KEY,
    AZURE_SPEECH_REGION,
)

SUPPORTED_AUDIO_EXTENSIONS = {
    "mp3", "wav", "wma", "aac", "ogg",
    "flac", "alaw", "ulaw", "mp4",
    "amr", "webm", "3gp", "3g2"
}


def is_audio(filename: str) -> bool:
    """Check if file is audio."""
    return filename.split(".")[-1] in SUPPORTED_AUDIO_EXTENSIONS


def process(file: UploadFile) -> str:
    """Process audio file and return its contents."""
    speech_config = SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_SPEECH_REGION)
    speech_recognizer = SpeechRecognizer(speech_config=speech_config)
    result = speech_recognizer.recognize_once_async().get()
    return result.text
