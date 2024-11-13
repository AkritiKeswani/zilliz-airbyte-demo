from fastapi import FastAPI

# Define the FastAPI application
app = FastAPI()

# Example route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
