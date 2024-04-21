<div align="center">
    
# 📦 Chat Nio Blob Service

**File Service for Chat Nio**

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Deeptrain-Community/chatnio-blob-service)

</div>

## Supported File Types
- Text
- Image (_require vision models_)
- Audio (_require Azure Speech to Text Service_)
- Docx (_not support .doc_)
- Pdf
- Pptx (_not support doc_)
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
    "file": "file"
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
- `MAX_FILE_SIZE`: Max File Size MiB (Default: No Limit)
  - Tips: Size limit is also depend on the server configuration (e.g. Nginx/Apache Config, Vercel Free Plan Limit **5MB** Body Size) 
- `CORS_ALLOW_ORIGINS`: CORS Allow Origins (Default: `*`)
  - e.g.: *http://localhost:3000,https://example.com*
- `AZURE_SPEECH_KEY`: Azure Speech to Text Service Key (Required for Audio Support)
- `AZURE_SPEECH_REGION`: Azure Speech to Text Service Region (Required for Audio Support)

## Image Storage Config
1. ✨ No Storage (Default)
   - [x] Base64 Encoding
   - [x] No Storage Required & No External Dependencies
   - [x] Support Serverless Deployment **Without Storage** (e.g. Vercel)

2. 📁 Local Storage
   - [ ] **Require Server Environment** (e.g. VPS, Docker)
   - [x] Support Direct URL Access
   - [x] Payless Storage Cost
   - Config:
     - set env `STORAGE_TYPE` to `local` (e.g. `STORAGE_TYPE=local`)
     - set env `LOCAL_STORAGE_DOMAIN` to your deployment domain (e.g. `LOCAL_STORAGE_DOMAIN=http://blob-service.onrender.com`)
     - if you are using Docker, you need to mount volume `/static` to the host (e.g. `-v /path/to/static:/static`)
     
3. 🚀 AWS S3 Storage
   - [ ] **Payment Storage Cost**
   - [x] Support Direct URL Access
   - [x] China Mainland User Friendly
   - Config:
     - set env `STORAGE_TYPE` to `s3` (e.g. `STORAGE_TYPE=s3`)
     - set env `AWS_ACCESS_KEY_ID` to your AWS Access Key ID
     - set env `AWS_SECRET_ACCESS_KEY` to your AWS Secret Access Key
     - set env `AWS_S3_BUCKET` to your AWS S3 Bucket Name
     - set env `AWS_S3_REGION` to your AWS S3 Region
     - set env `AWS_S3_DOMAIN` to your AWS S3 Domain (e.g. `https://s3.amazonaws.com`)