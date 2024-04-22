from fastapi import UploadFile
import boto3
from botocore.exceptions import ClientError, NoCredentialsError, PartialCredentialsError
from botocore.client import Config

from store.utils import store_filename
from config import (
    S3_BUCKET, S3_ACCESS_KEY, S3_SECRET_KEY, S3_REGION, S3_API, S3_DOMAIN, S3_SPACE, S3_SIGN_VERSION,
)


def create_s3_client():
    config = Config(signature_version=S3_SIGN_VERSION) if S3_SIGN_VERSION else None
    if S3_DOMAIN and len(S3_DOMAIN) > 0:
        # Cloudflare R2 Storage
        return boto3.client(
            "s3",
            aws_access_key_id=S3_ACCESS_KEY,
            aws_secret_access_key=S3_SECRET_KEY,
            endpoint_url=S3_API,
            config=config,
        )

    return boto3.client(
        "s3",
        region_name=S3_REGION,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY,
        config=config,
    )


async def process_s3(file: UploadFile) -> str:
    """Process image and return its s3 url."""

    filename = store_filename(file.filename)

    try:
        client = create_s3_client()
        client.upload_fileobj(
            file.file,
            S3_BUCKET,
            filename,
            ExtraArgs={"ACL": "public-read"},
        )

        return f"{S3_SPACE}/{filename}"
    except (NoCredentialsError, PartialCredentialsError) as e:
        raise ValueError(f"AWS credentials not found: {e}")
    except ClientError as e:
        raise ValueError(f"AWS S3 error: {e}")
    except Exception as e:
        raise ValueError(f"S3 error: {e}")
