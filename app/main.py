from fastapi import FastAPI
from app.config import Settings
from app.models import PayloadModel
from app.controller import fetch_data_from_s3

app = FastAPI()
settings = Settings()


@app.get("/")
def read_root():
    return {"status": "Dockerization successful!"}


@app.post("/test-route")
def read_item(payload: PayloadModel):
    S3_ACCESS_KEY = settings.S3_ACCESS_KEY
    S3_SECRET_ACCESS_KEY = settings.S3_SECRET_ACCESS_KEY
    response = fetch_data_from_s3(payload, S3_ACCESS_KEY, S3_SECRET_ACCESS_KEY)
    return response
