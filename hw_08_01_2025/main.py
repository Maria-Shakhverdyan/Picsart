from fastapi import FastAPI
from db.connection import db_connection
from routes.books import router as books_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await db_connection.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await db_connection.disconnect()

app.include_router(books_router, prefix="/books", tags=["Books"])