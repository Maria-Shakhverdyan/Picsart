from fastapi import APIRouter, HTTPException, status, Depends
from pymongo import ReturnDocument
from bson import ObjectId

from db.connection import db_connection
from db.models import BookModel
from schemas.book import BookCreate, BookUpdateStatus

router = APIRouter()

@router.post("/", response_model=BookModel)
async def add_book(book: BookCreate):
    book_data = book.dict()
    book_data["status"] = "available"
    result = await db_connection.db.books.insert_one(book_data)
    return {**book_data, "_id": str(result.inserted_id)}

@router.get("/", response_model=list[BookModel])
async def get_all_books():
    books = await db_connection.db.books.find().to_list(100)
    return books

@router.get("/{book_id}", response_model=BookModel)
async def get_book_by_id(book_id: str):
    if not ObjectId.is_valid(book_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    book = await db_connection.db.books.find_one({"_id": ObjectId(book_id)})
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=BookModel)
async def update_book_status(book_id: str, status_update: BookUpdateStatus):
    if not ObjectId.is_valid(book_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    updated_book = await db_connection.db.books.find_one_and_update(
        {"_id": ObjectId(book_id)},
        {"$set": {"status": status_update.status}},
        return_document=ReturnDocument.AFTER
    )
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/{book_id}")
async def delete_book(book_id: str):
    if not ObjectId.is_valid(book_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    result = await db_connection.db.books.delete_one({"_id": ObjectId(book_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": "Book deleted successfully"}