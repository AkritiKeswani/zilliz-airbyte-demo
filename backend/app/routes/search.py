from fastapi import APIRouter
from app.services.milvus import search_milvus

router = APIRouter()

@router.post("/")
async def search_task(vector: list, top_k: int = 5):
    results = search_milvus(vector, top_k)
    return {"results": results}
