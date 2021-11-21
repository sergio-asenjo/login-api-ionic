from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    nombre: str
    password: str
    email: Optional[str] = None