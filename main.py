from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer('google/embeddinggemma-300m')

class TextRequest(BaseModel):
    text: str

@app.post('/embed')
def embed_text(req: TextRequest):
    embedding = model.encode(req.text)
    return {"embedding": embedding.tolist()}
