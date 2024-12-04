from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    email: EmailStr
    password: str = Field(..., min_length=6)

class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    user_id: int
