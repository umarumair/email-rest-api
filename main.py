from typing import List

from fastapi import FastAPI

from models import Email

app = FastAPI()


db: List[Email] = [
    Email(id=1,receiver_email="abc@a.com", subject = "hi", body_text="Hello World"),
    Email(id=2,receiver_email="abc@ab.com", subject = "hi", body_text="Hello World"),
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/emails")
async def fetch_emails():
    return db


