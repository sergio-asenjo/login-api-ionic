from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_somenthing():
    return {"msg": "Hello World!"}