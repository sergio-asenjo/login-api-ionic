from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes_user import user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)

@app.get("/")
async def index():
    return {"message": "Hello, World!"}