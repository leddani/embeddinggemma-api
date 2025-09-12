# EmbeddingGemma API (FastAPI)

API për të gjeneruar embeddings me modelin Google EmbeddingGemma.

## Endpoints
- **POST /embed**
  - Body: `{ "text": "Teksti yt këtu" }`
  - Response: `{ "embedding": [ ... ] }`

## Deploy në Coolify
1. Ngarko këtë folder në një repo në GitHub.
2. Në Coolify, krijo një "New App" dhe lidh repo-n.
3. Zgjidh "Dockerfile" si metodë deploy.
4. Deploy dhe API do të jetë online në portin 8000.

## Testo lokalisht
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Shembull kërkese me curl
```bash
curl -X POST http://localhost:8000/embed -H "Content-Type: application/json" -d '{"text": "Pershendetje nga Shqipëria!"}'
```
