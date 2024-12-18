from fastapi import APIRouter, Depends, HTTPException, status
from models.schemas import MovieCreate, MovieOut
from typing import List
from utils.auth_utils import decode_token
from fastapi.security import OAuth2PasswordBearer

movies_router = APIRouter(prefix="/movies", tags=["movies"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

movies_db = []

@movies_router.get("/", response_model=List[MovieOut])
def get_movies(genre: str = None, rating: float = None):
    result = movies_db
    if genre:
        result = [m for m in result if m["genre"].lower() == genre.lower()]
    if rating is not None:
        result = [m for m in result if m["rating"] == rating]
    return result

@movies_router.post("/", response_model=MovieOut, status_code=status.HTTP_201_CREATED)
def create_movie(movie: MovieCreate, token: str = Depends(oauth2_scheme)):
    username = decode_token(token)
    
    if any(m["title"].lower() == movie.title.lower() for m in movies_db):
        raise HTTPException(status_code=409, detail=f"Movie with title '{movie.title}' already exists")
    
    new_movie = movie.dict()
    new_movie["created_by"] = username
    new_movie["id"] = len(movies_db) + 1
    
    movies_db.append(new_movie)
    return new_movie
