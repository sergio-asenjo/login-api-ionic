from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    nombre: str
    password: Optional[str] = None
    email: Optional[str] = None