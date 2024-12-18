from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    username: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    email: EmailStr

class MovieBase(BaseModel):
    title: str = Field(..., min_length=5, max_length=100)
    genre: str = Field(..., min_length=2, max_length=100)
    rating: float = Field(..., ge=0.0, le=10.0)
    
class MovieCreate(MovieBase):
    pass

class MovieOut(MovieBase):
    pass

class RentalBase(BaseModel):
    movie_title: str
    rental_duration: int = Field(..., ge=1)
