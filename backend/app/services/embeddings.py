import openai
from app.core.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_embedding(text: str):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response["data"][0]["embedding"]
