from os import environ

EXPOSE = "https://blob.chatnio.net"
SERVICE = "https://www.chatnio.net"
MAX_FILE_SIZE = 1024 ** 2 * 25  # deprecated in favor of `upload_max_size` in nginx.conf
CORS_ALLOW_ORIGINS = ["*"]

AZURE_SPEECH_KEY = environ.get("AZURE_SPEECH_KEY")
AZURE_SPEECH_REGION = environ.get("AZURE_SPEECH_REGION")
ENABLE_AZURE_SPEECH = AZURE_SPEECH_KEY and AZURE_SPEECH_REGION
