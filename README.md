<div align="center">
    
# 📦 Chat Nio Blob Service

**File Service for Chat Nio**

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Deeptrain-Community/chatnio-blob-service)

</div>

## Features
- ⚡ **Out-of-the-Box**: No External Dependencies Required & Support Vercel/Render One-Click Deployment
- ⭐ **Multiple File Types**: Support Text, Pdf, Docx, Excel, Image, Audio etc.
- 📦 **Multiple Storage Options**: Base64, Local, S3, Cloudflare R2, Min IO, Telegram CDN etc.
- 🔍 **OCR Support**: Extract Text from Image (Require Paddle OCR API)
- 🔊 **Audio Support**: Convert Audio to Text (Require Azure Speech to Text Service)

## Supported File Types
- Text
- Image (_require vision models_)
- Audio (_require Azure Speech to Text Service_)
- Docx (_not support .doc_)
- Pdf
- Pptx (_not support .ppt_)
- Xlsx (_support .xls_)


## Run
```shell
pip install -r requirements.txt
uvicorn main:app --reload
```
Then the service will be running on `http://localhost:8000`

## Deploy
```shell
uvicorn main:app
```

## Using Docker
> Image: `programzmh/chatnio-blob-service`

```shell
docker run -p 8000:8000 programzmh/chatnio-blob-service

# with environment variables
# docker run -p 8000:8000 -e AZURE_SPEECH_KEY="..." -e AZURE_SPEECH_REGION="..." programzmh/chatnio-blob-service


# if you are using `local` storage type, you need to mount volume (/static) to the host
# docker run -p 8000:8000 -v /path/to/static:/static programzmh/chatnio-blob-service
```

## API
`POST` `/upload` Upload a file
```json
{
    "file": "file",
    "model": "gpt-4-turbo-preview" // optional (for ocr models detection)
}
```

Response

```json
{
  "status": true,
  "content": "...",
  "error": ""
}
```

## Environment Variables
### 🎨 General Config (Optional)

- `PDF_MAX_IMAGES`: Max Images Extracted from a PDF File
    - **0**: Never Extract Images
    - **-1**: Extract All Images
    - **other**: Extract Top N Images
    - *Tips: The extracted images will be **treated as a normal image** file and directly processed*.
- `MAX_FILE_SIZE`: Max Uploaded File Size MiB (Default: No Limit)
  - *Tips: Size limit is also depend on the server configuration (e.g. Nginx/Apache Config, Vercel Free Plan Limit **5MB** Body Size)*
- `CORS_ALLOW_ORIGINS`: CORS Allow Origins (Default: `*`)
  - e.g.: *http://localhost:3000,https://example.com*
- `AZURE_SPEECH_KEY`: Azure Speech to Text Service Key (Required for Audio Support)
- `AZURE_SPEECH_REGION`: Azure Speech to Text Service Region (Required for Audio Support)



### 🖼 Image Storage Config (Optional)
> [!NOTE]
> **When OCR is enabled, the service will firstly using OCR then store the images.**
>
> **You can configure the OCR Advanced Config to control the OCR Models Filtering.**

1. ✨ No Storage (Default)
   - [x] **No Storage Required & No External Dependencies**
   - [x] Base64 Encoding/Decoding
   - [x] Support Serverless Deployment **Without Storage** (e.g. Vercel)

2. 📁 Local Storage
   - [ ] **Require Server Environment** (e.g. VPS, Docker)
   - [x] Support Direct URL Access
   - [x] Payless Storage Cost
   - Config:
     - set env `STORAGE_TYPE` to `local` (e.g. `STORAGE_TYPE=local`)
     - set env `LOCAL_STORAGE_DOMAIN` to your deployment domain (e.g. `LOCAL_STORAGE_DOMAIN=http://blob-service.onrender.com`)
     - if you are using Docker, you need to mount volume `/static` to the host (e.g. `-v /path/to/static:/static`)
     
3. 🚀 [AWS S3](https://aws.amazon.com/s3)
   - [ ] **Payment Storage Cost**
   - [x] Support Direct URL Access
   - [x] China Mainland User Friendly
   - Config:
     - set env `STORAGE_TYPE` to `s3` (e.g. `STORAGE_TYPE=s3`)
     - set env `S3_ACCESS_KEY` to your AWS Access Key ID
     - set env `S3_SECRET_KEY` to your AWS Secret Access Key
     - set env `S3_BUCKET` to your AWS S3 Bucket Name
     - set env `S3_REGION` to your AWS S3 Region

4. 🔔 [Cloudflare R2](https://www.cloudflare.com/zh-cn/developer-platform/r2)
   - [x] **Free Storage Quota ([10GB Storage & Zero Outbound Cost]((https://developers.cloudflare.com/r2/pricing/)))**
   - [x] Support Direct URL Access
   - Config *(S3 Compatible)*:
     - set env `STORAGE_TYPE` to `s3` (e.g. `STORAGE_TYPE=s3`)
     - set env `S3_ACCESS_KEY` to your Cloudflare R2 Access Key ID
     - set env `S3_SECRET_KEY` to your Cloudflare R2 Secret Access Key
     - set env `S3_BUCKET` to your Cloudflare R2 Bucket Name
     - set env `S3_DOMAIN` to your Cloudflare R2 Domain Name (e.g. `https://<account-id>.r2.cloudflarestorage.com`)
     - set env `S3_DIRECT_URL_DOMAIN` to your Cloudflare R2 Public URL Access Domain Name ([Open Public URL Access](https://developers.cloudflare.com/r2/buckets/public-buckets/), e.g. `https://pub-xxx.r2.dev`)

5. 📦 [Min IO](https://min.io)
    - [x] **Self Hosted**
    - [x] Reliable & Flexible Storage
    - Config *(S3 Compatible)*:
      - set env `STORAGE_TYPE` to `s3` (e.g. `STORAGE_TYPE=s3`)
      - set env `S3_SIGN_VERSION` to `s3v4` (e.g. `S3_SIGN_VERSION=s3v4`)
      - set env `S3_ACCESS_KEY` to your Min IO Access Key ID
      - set env `S3_SECRET_KEY` to your Min IO Secret Access Key
      - set env `S3_BUCKET` to your Min IO Bucket Name
      - set env `S3_DOMAIN` to your Min IO Domain Name (e.g. `https://oss.example.com`)
      - *[Optional] If you are using CDN, you can set `S3_DIRECT_URL_DOMAIN` to your Min IO Public URL Access Domain Name (e.g. `https://cdn-hk.example.com`)*

6. ❤ [Telegram CDN](https://github.com/csznet/tgState)
    - [x] **Free Storage (Rate Limit)**
    - [x] Support Direct URL Access *(China Mainland User Unfriendly)*
    - [x] Config:
      - set env `STORAGE_TYPE` to `tg` (e.g. `STORAGE_TYPE=tg`)
      - set env `TG_ENDPOINT` to your TG-STATE Endpoint (e.g. `TG_ENDPOINT=https://tgstate.vercel.app`)
      - *[Optional] if you are using password authentication, you can set `TG_PASSWORD` to your TG-STATE Password*



### 🔍 OCR Config (Optional)
> [!NOTE]
> OCR Support is based on [PaddleOCR API](https://github.com/cgcel/PaddleOCRFastAPI), please deploy the API to use OCR feature.
> 
> When OCR is enabled, the service will automatically extract text from the image and **skip the original image storage solution** below.

- `OCR_ENABLED` Image OCR Enabled (`1` for **Enabled**, `0` for **Disabled**, Default is **Disabled**)
- `OCR_ENDPOINT` Paddle OCR Endpoint ([Deploy PaddleOCR API](https://github.com/cgcel/PaddleOCRFastAPI))
    - e.g.: *http://example.com:8000*

Advanced OCR Config:
- `OCR_SKIP_MODELS`: Skip OCR Models List (Commonly for Vision Models)
    - e.g.: *gpt-4-v,gpt-4-vision-preview,gpt-4-turbo*, then the service will skip these models and directly store the image.
      - Tips: Each model has character inclusion matching, so when you set `gpt-4-v` model, it will skip all models that contain **gpt-4-v** (like azure-**gpt-4-v**ision-preview, **gpt-4-v**ision-preview will be also matched).
- `OCR_SPEC_MODELS`: Specific OCR Models List (Commonly for Non-Vision Models)
    - then although the image has marked as `SKIP_MODELS`, the service will still ocr process the image with this model first.
    - for example, when you set `gpt-4-turbo` to `SKIP_MODELS` (because `gpt-4-turbo` support vision and don't need to use OCR, `gpt-4-turbo-preview` cannot vision and need OCR), commonly the **gpt-4-turbo**-preview will be marked as **gpt-4-turbo** and skipped, then you can set `gpt-4-turbo-preview` to `SPEC_MODELS` to force OCR process.

EXAMPLE OCR Config:
```env
OCR_ENABLED=1
OCR_ENDPOINT=http://example.com:8000
OCR_SKIP_MODELS=vision,gpt-4-v,gpt-4-all,gpt-4-vision-preview,gpt-4-1106-vision-preview,gpt-4-turbo,gemini-pro-vision,gemini-1.5-pro,claude-3,glm-4v
OCR_SPEC_MODELS=gpt-4-turbo-preview,claude-3-haiku
```
