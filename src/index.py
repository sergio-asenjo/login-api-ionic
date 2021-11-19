from fastapi import FastAPI
from src.routes_user import user

app = FastAPI()

app.include_router(user)

@app.get("/")
async def index():
    return {"message": "Hello, World!"}