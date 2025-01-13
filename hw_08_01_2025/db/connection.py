import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.database import Database
from dotenv import load_dotenv

load_dotenv()

class DatabaseConnection:
    def __init__(self):
        self.client = None
        self.db: Database = None

    async def connect(self):
        mongo_uri = os.getenv("MONGO_URI")
        mongo_db_name = os.getenv("MONGO_DB_NAME")

        if not mongo_uri or not mongo_db_name:
            raise ValueError("Database connection parameters are missing in .env file.")

        self.client = AsyncIOMotorClient(mongo_uri)
        self.db = self.client[mongo_db_name]

    async def disconnect(self):
        if self.client:
            self.client.close()

db_connection = DatabaseConnection()