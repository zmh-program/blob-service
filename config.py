from os import environ

CORS_ALLOW_ORIGINS = ["*"]  # CORS Allow Origins
if environ.get("CORS_ALLOW_ORIGINS") and len(environ.get("CORS_ALLOW_ORIGINS")) > 0:
    CORS_ALLOW_ORIGINS = environ.get("CORS_ALLOW_ORIGINS").split(",")

PDF_MAX_IMAGES = int(environ.get("PDF_MAX_IMAGES", 0))  # The maximum number of images to extract from a PDF file

AZURE_SPEECH_KEY = environ.get("AZURE_SPEECH_KEY")  # Azure Speech Key
AZURE_SPEECH_REGION = environ.get("AZURE_SPEECH_REGION")  # e.g. "eastus"
ENABLE_AZURE_SPEECH = AZURE_SPEECH_KEY and AZURE_SPEECH_REGION

MAX_FILE_SIZE = float(environ.get("MAX_FILE_SIZE", -1))  # Max File Size (unit: MiB)

STORAGE_TYPE = environ.get("STORAGE_TYPE", "common").lower()  # Storage Type
LOCAL_STORAGE_DOMAIN = environ.get("LOCAL_STORAGE_DOMAIN", "").rstrip("/")  # Local Storage Domain

S3_BUCKET = environ.get("S3_BUCKET", "")  # S3 Bucket
S3_ACCESS_KEY = environ.get("S3_ACCESS_KEY", "")  # S3 Access Key
S3_SECRET_KEY = environ.get("S3_SECRET_KEY", "")  # S3 Secret Key
S3_REGION = environ.get("S3_REGION", "")  # S3 Region
S3_DOMAIN = environ.get("S3_DOMAIN", "").rstrip("/")  # S3 Domain (Optional)
S3_DIRECT_URL_DOMAIN = environ.get("S3_DIRECT_URL_DOMAIN", "").rstrip("/")  # S3 Direct/Proxy URL Domain (Optional)
S3_SIGN_VERSION = environ.get("S3_SIGN_VERSION", None)  # S3 Sign Version

S3_API = S3_DOMAIN or f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com"  # S3 API
S3_SPACE = S3_DIRECT_URL_DOMAIN or S3_API  # S3 Image URL Domain

TG_ENDPOINT = environ.get("TG_ENDPOINT", "").rstrip("/")  # Telegram Endpoint
TG_PASSWORD = environ.get("TG_PASSWORD", "")  # Telegram Password

TG_API = TG_ENDPOINT + "/api" + (f"?pass={TG_PASSWORD}" if TG_PASSWORD and len(TG_PASSWORD) > 0 else "")

OCR_ENDPOINT = environ.get("OCR_ENDPOINT", "").rstrip("/")  # OCR Endpoint
OCR_ENABLED = int(environ.get("OCR_ENABLED", 0)) == 1  # OCR Enabled
OCR_SKIP_MODELS = environ.get("OCR_SKIP_MODELS", "").split(",")  # OCR Skip Models
OCR_SPEC_MODELS = environ.get("OCR_SPEC_MODELS", "").split(",")  # OCR Specific Models
