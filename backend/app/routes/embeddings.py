from fastapi import APIRouter
import openai

router = APIRouter()

@router.post("/")
async def generate_embedding(text: str):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return {"embedding": response["data"][0]["embedding"]}
