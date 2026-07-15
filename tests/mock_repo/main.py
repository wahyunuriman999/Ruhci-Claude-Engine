
from fastapi import FastAPI
import uvicorn
from .database import engine

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
