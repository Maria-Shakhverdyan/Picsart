from pydantic import BaseModel, Field
from typing import List

class BookCreate(BaseModel):
    title: str
    author: str
    genre: List[str]
    rating: int
    pages: int

class BookUpdateStatus(BaseModel):
    status: str = Field(..., regex="^(available|borrowed)$")