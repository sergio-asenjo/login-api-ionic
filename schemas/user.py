from pydantic import BaseModel

class User(BaseModel):
    nombre: str
    password: str
    email: str