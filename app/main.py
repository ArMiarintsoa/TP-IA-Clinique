from typing import Union
from app.text.routers import router as text_router
from fastapi import FastAPI

app = FastAPI(title="Text editor API")

app.include_router(text_router)