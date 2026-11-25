import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import geo  # thêm router mới vào đây

app = FastAPI(title="MarLens API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "http://localhost:5173").split(","),
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok"}


app.include_router(geo.router, prefix="/api")
