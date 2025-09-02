# app.py
from fastapi import FastAPI

app = FastAPI(title="My First API")

@app.get("/")
def root():
    return {"status": "ok"}

# Запуск: uvicorn app:app --reload
