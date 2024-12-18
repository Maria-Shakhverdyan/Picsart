from fastapi import FastAPI, Request
from routers.auth import auth_router
from routers.movies import movies_router
from dotenv import load_dotenv
from routers.rentals import rentals_router
from utils.auth_utils import set_secret_key
import os
import time

load_dotenv()

app = FastAPI()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "defaultsecret")
set_secret_key(JWT_SECRET_KEY)

@app.middleware("http")
async def log_requests(request: Request, call):
    start_time = time.time()
    response = await call(request)
    process_t = (time.time() - start_time)
    print(f"{request.method} {request.url} completed ={process_t:.1f}, status_code={response.status_code}")
    return response

app.include_router(auth_router)
app.include_router(movies_router)
app.include_router(rentals_router)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="127.0.0.1", port=port)
