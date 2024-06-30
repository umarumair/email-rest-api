from typing import List

from fastapi import FastAPI, HTTPException

from models import Email

app = FastAPI()

db: List[Email] = [
    Email(receiver_email="demo@gmail.com", subject="Demo", body_text="Hello world, how are you"),
    Email(receiver_email="test@outlook.com", subject="Test", body_text="Hello this is the body of email"),
]


@app.get("/")
async def root():
    return {"REST API": "go to /api/emails to fetch emails", "endpoints": "go to /docs for interactive API docs"}


@app.get("/api/emails")
async def fetch_emails():
    return db


@app.post("/api/emails")
async def add_email(email: Email):
    db.append(email)
    return {"message": "Email added", "id": email.id}


@app.delete("/api/emails/{id}")
async def delete_email(id: int):
    for email in db:
        if email.id == id:
            db.remove(email)
            return {"message": "Email removed", "id": email.id}
    raise HTTPException(status_code=404, detail=f"Email with {id} not found")
