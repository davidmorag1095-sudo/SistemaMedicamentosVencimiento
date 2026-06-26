from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.database import init_db

app = FastAPI(title="Sistema Medicamentos API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()
