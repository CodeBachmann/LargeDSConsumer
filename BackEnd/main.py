from sys import prefix
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from API.routers import upload

app = FastAPI(
)

origins = [
    "http://localhost:5173",  # porta do frontend React/Uppy
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # permite requisições do frontend
    allow_credentials=True,
    allow_methods=["*"],         # permite POST, OPTIONS, GET, etc
    allow_headers=["*"],         # permite todos os headers
)

prefix="/api/v1"

app.include_router(upload.router, prefix=prefix)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)