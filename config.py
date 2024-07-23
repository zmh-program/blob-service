from os import environ


def to_str(key: str, default: str = "") -> str:
    """Converts string to string."""

    value = environ.get(key, default)
    return value.strip()


def to_none_str(key: str, default: str = None) -> str:
    """Converts string to string."""

    value = environ.get(key, default)
    return value.strip() if value else None


def to_endpoint(key: str, default: str = "") -> str:
    """Converts string to string."""
    return to_str(key, default).rstrip("/")


def to_list(key: str, default: list) -> list:
    """Converts comma-separated string to list."""
    key = to_str(key, "")
    if not key:
        return default

    return [item for item in key.split(",") if item]


def to_bool(key: str, default: bool) -> bool:
    """Converts string to bool."""
    value = to_str(key, "")
    if not value:
        return default

    return value.lower() == "true" or value == "1"


def to_float(key: str, default: float) -> float:
    """Converts string to float."""
    value = to_str(key, "")
    if not value:
        return default

    return float(value)


def to_int(value: str, default: int) -> int:
    """Converts string to int."""
    value = to_str(value, "")
    if not value:
        return default

    return int(value)


# General Config
CORS_ALLOW_ORIGINS = to_list("CORS_ALLOW_ORIGINS", ["*"])  # CORS Allow Origins
MAX_FILE_SIZE = to_float("MAX_FILE_SIZE", -1)  # Max File Size
PDF_MAX_IMAGES = to_int("PDF_MAX_IMAGES", 10)  # PDF Max Images
AZURE_SPEECH_KEY = to_str("AZURE_SPEECH_KEY")  # Azure Speech Key
AZURE_SPEECH_REGION = to_str("AZURE_SPEECH_REGION")  # Azure Speech Region
ENABLE_AZURE_SPEECH = AZURE_SPEECH_KEY and AZURE_SPEECH_REGION  # Enable Azure Speech

# Storage Config
STORAGE_TYPE = to_str("STORAGE_TYPE", "common")  # Storage Type
LOCAL_STORAGE_DOMAIN = to_str("LOCAL_STORAGE_DOMAIN", "").rstrip("/")  # Local Storage Domain
S3_BUCKET = to_str("S3_BUCKET", "")  # S3 Bucket
S3_ACCESS_KEY = to_str("S3_ACCESS_KEY", "")  # S3 Access Key
S3_SECRET_KEY = to_str("S3_SECRET_KEY", "")  # S3 Secret Key
S3_REGION = to_str("S3_REGION", "")  # S3 Region
S3_DOMAIN = to_endpoint("S3_DOMAIN", "")  # S3 Domain (Optional)
S3_DIRECT_URL_DOMAIN = to_endpoint("S3_DIRECT_URL_DOMAIN", "")  # S3 Direct/Proxy URL Domain (Optional)
S3_SIGN_VERSION = to_none_str("S3_SIGN_VERSION")  # S3 Sign Version
S3_API = S3_DOMAIN or f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com"  # S3 API
S3_SPACE = S3_DIRECT_URL_DOMAIN or S3_API  # S3 Image URL Domain
TG_ENDPOINT = to_endpoint("TG_ENDPOINT", "")  # Telegram Endpoint
TG_PASSWORD = to_str("TG_PASSWORD", "")  # Telegram Password
TG_API = TG_ENDPOINT + "/api" + (f"?pass={TG_PASSWORD}" if TG_PASSWORD and len(TG_PASSWORD) > 0 else "")  # Telegram API

# OCR Config
OCR_ENDPOINT = to_endpoint("OCR_ENDPOINT", "")  # OCR Endpoint
OCR_SKIP_MODELS = to_list("OCR_SKIP_MODELS", [])  # OCR Skip Models
OCR_SPEC_MODELS = to_list("OCR_SPEC_MODELS", [])  # OCR Specific Models
