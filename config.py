from os import environ

CORS_ALLOW_ORIGINS = ["*"]  # CORS Allow Origins
if environ.get("CORS_ALLOW_ORIGINS") and len(environ.get("CORS_ALLOW_ORIGINS")) > 0:
    CORS_ALLOW_ORIGINS = environ.get("CORS_ALLOW_ORIGINS").split(",")

AZURE_SPEECH_KEY = environ.get("AZURE_SPEECH_KEY")  # Azure Speech Key
AZURE_SPEECH_REGION = environ.get("AZURE_SPEECH_REGION")  # e.g. "eastus"
ENABLE_AZURE_SPEECH = AZURE_SPEECH_KEY and AZURE_SPEECH_REGION

MAX_FILE_SIZE = float(environ.get("MAX_FILE_SIZE", -1))  # Max File Size (unit: MiB)
