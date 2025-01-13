from bson import ObjectId
from pydantic import BaseModel, Field
from typing import List

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

class BookModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    author: str
    genre: List[str]
    rating: int
    pages: int
    status: str = "available"

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Algorithms",
                "author": "Cormen",
                "genre": ["horror"],
                "rating": 5,
                "pages": 550,
                "status": "available"
            }
        }