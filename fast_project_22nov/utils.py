import json
from aiofiles import open as aio_open
from typing import Any, List
from dotenv import load_dotenv
import os
from errors import FileError

load_dotenv()

USERS_FILE = os.getenv("USERS_FILE", "users.json")
TASKS_FILE = os.getenv("TASKS_FILE", "tasks.json")


async def read_json(file_name: str) -> List[Any]:
    try:
        async with aio_open(file_name, "r") as file:
            content = await file.read()
            return json.loads(content) if content else []
    except FileNotFoundError:
        async with aio_open(file_name, "w") as file:
            await file.write("[]")
        return []
    except json.JSONDecodeError:
        raise FileError(detail=f"File {file_name} is corrupted.")


async def write_json(file_name: str, data: List[Any]) -> None:
    async with aio_open(file_name, "w") as file:
        await file.write(json.dumps(data, indent=4))
