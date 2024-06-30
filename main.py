from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from models import Email

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>Email REST API</title>
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>REST API in Serverless Environment</h1>
            <h2> Fetch emails from API</h2>
            <a href="/api/emails">Get emails from API</a>
            <p>Click Below links to interact with API endpoints</p>
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
        </div>
    </body>
</html>
"""

db: List[Email] = [
    Email(receiver_email="demo@gmail.com", subject="Demo", body_text="Hello world, how are you"),
    Email(receiver_email="test@outlook.com", subject="Test", body_text="Hello this is the body of email"),
]


@app.get("/")
async def root():
    return HTMLResponse(html)


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
