from fastapi import APIRouter, Depends, HTTPException, status
from models.schemas import RentalBase
from typing import List
from utils.auth_utils import decode_token
from fastapi.security import OAuth2PasswordBearer

rentals_router = APIRouter(prefix="/rentals", tags=["rentals"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

from routers.movies import movies_db

rentals_db = {}

@rentals_router.post("/")
def rent_movie(rental: RentalBase, token: str = Depends(oauth2_scheme)):
    username = decode_token(token)
    
    movie_index = None
    for i, m in enumerate(movies_db):
        if m["title"].lower() == rental.movie_title.lower():
            movie_index = i
            break
    
    if movie_index is None:
        raise HTTPException(status_code=404, detail="Movie not found or already rented.")
    
    movie = movies_db.pop(movie_index)
    
    if username not in rentals_db:
        rentals_db[username] = []
        
    rented_movie = {
        "title": movie["title"],
        "genre": movie["genre"],
        "rating": movie["rating"],
        "rental_duration": rental.rental_duration
    }
    rentals_db[username].append(rented_movie)
    
    return {"message": f"Movie '{rental.movie_title}' rented successfully for {rental.rental_duration} days."}


@rentals_router.get("/")
def get_rental_history(token: str = Depends(oauth2_scheme)):
    username = decode_token(token)
    return rentals_db.get(username, [])
