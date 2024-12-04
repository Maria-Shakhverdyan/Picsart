from fastapi import FastAPI
from models import User, Task
from utils import read_json, write_json, USERS_FILE, TASKS_FILE
from errors import ValidationError, NotFoundError
from typing import List
import uvicorn
from dotenv import load_dotenv
import os

app = FastAPI()


@app.post("/register", response_model=User)
async def register_user(user: User):
    users = await read_json(USERS_FILE)
    if any(u["email"] == user.email for u in users):
        raise ValidationError(detail="Email already exists.")
    user.id = len(users) + 1
    users.append(user.dict())
    await write_json(USERS_FILE, users)
    return user


@app.post("/login")
async def login_user(email: str, password: str):
    users = await read_json(USERS_FILE)
    user = next((u for u in users if u["email"] == email and u["password"] == password), None)
    if not user:
        raise ValidationError(detail="Invalid email or password.")
    return {"message": "Login successful"}


@app.get("/users", response_model=List[User])
async def get_users():
    return await read_json(USERS_FILE)


@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    users = await read_json(USERS_FILE)
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise NotFoundError(detail="User not found.")
    return user


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: User):
    users = await read_json(USERS_FILE)
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise NotFoundError(detail="User not found.")
    user.update(updated_user.dict(exclude={"id"}))
    await write_json(USERS_FILE, users)
    return updated_user


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    users = await read_json(USERS_FILE)
    updated_users = [u for u in users if u["id"] != user_id]
    if len(updated_users) == len(users):
        raise NotFoundError(detail="User not found.")
    await write_json(USERS_FILE, updated_users)
    return {"message": "User deleted successfully."}


@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    users = await read_json(USERS_FILE)
    if not any(u["id"] == task.user_id for u in users):
        raise ValidationError(detail="User ID does not exist.")
    tasks = await read_json(TASKS_FILE)
    task.id = len(tasks) + 1
    tasks.append(task.dict())
    await write_json(TASKS_FILE, tasks)
    return task


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return await read_json(TASKS_FILE)


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    tasks = await read_json(TASKS_FILE)
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        raise NotFoundError(detail="Task not found.")
    return task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    tasks = await read_json(TASKS_FILE)
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        raise NotFoundError(detail="Task not found.")
    task.update(updated_task.dict(exclude={"id"}))
    await write_json(TASKS_FILE, tasks)
    return updated_task


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    tasks = await read_json(TASKS_FILE)
    updated_tasks = [t for t in tasks if t["id"] != task_id]
    if len(updated_tasks) == len(tasks):
        raise NotFoundError(detail="Task not found.")
    await write_json(TASKS_FILE, updated_tasks)
    return {"message": "Task deleted successfully."}

if __name__ == "__main__":
    
    load_dotenv()

    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))

    uvicorn.run("main:app", host=host, port=port, reload=True)
