# chatnio-blob-service
File Service for Chat Nio

## Supported File Types
- Text
- Image
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
- `AZURE_SPEECH_KEY`: Azure Speech to Text Service Key
- `AZURE_SPEECH_REGION`: Azure Speech to Text Service Region
