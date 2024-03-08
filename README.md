# chatnio-blob-service
File Service for Chat Nio

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

Environment Variables
- `AZURE_SPEECH_KEY`: Azure Speech to Text Service Key (Required for Audio Support)
- `AZURE_SPEECH_REGION`: Azure Speech to Text Service Region (Required for Audio Support)
