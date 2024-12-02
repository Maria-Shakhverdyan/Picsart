from fastapi import FastAPI, HTTPException
from typing import List
import uvicorn

app = FastAPI()

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500}
]

# CRUD for /users
@app.get("/users", response_model=List[dict])
def get_users():
    return users

@app.get("/users/{user_id}", response_model=dict)
def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=dict)
def create_user(user: dict):
    user["id"] = max([u["id"] for u in users] + [0]) + 1
    users.append(user)
    return user

@app.put("/users/{user_id}", response_model=dict)
def update_user(user_id: int, updated_user: dict):
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.update(updated_user)
    return user

@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    users = [u for u in users if u["id"] != user_id]
    return {"message": f"User with ID {user_id} deleted"}

# CRUD for /products
@app.get("/products", response_model=List[dict])
def get_products():
    return products

@app.get("/products/{product_id}", response_model=dict)
def get_product(product_id: int):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products", response_model=dict)
def create_product(product: dict):
    product["id"] = max([p["id"] for p in products] + [0]) + 1
    products.append(product)
    return product

@app.put("/products/{product_id}", response_model=dict)
def update_product(product_id: int, updated_product: dict):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    product.update(updated_product)
    return product

@app.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int):
    global products
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    products = [p for p in products if p["id"] != product_id]
    return {"message": f"Product with ID {product_id} deleted"}

if __name__ == "__main__":
    uvicorn.run("fl:app", host="127.0.0.1", port=8080, reload=True)

