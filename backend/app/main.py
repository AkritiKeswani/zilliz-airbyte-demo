from fastapi import FastAPI
from app.routes import embeddings, search

app = FastAPI()

# Include routers
app.include_router(embeddings.router, prefix="/generate-embedding", tags=["Embedding"])
app.include_router(search.router, prefix="/search", tags=["Search"])

@app.get("/")
def root():
    return {"message": "Backend is running"}
