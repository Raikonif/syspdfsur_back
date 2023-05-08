from fastapi import FastAPI
from models import model
from config import engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = ["http://localhost:8081", "localhost:8081", "http://127.0.0.1:8081", "127.0.0.1:8081"]


@app.get("/")
async def home():
    return {"message": "Hello World"}
