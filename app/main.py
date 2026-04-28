# app/main.py

from fastapi import FastAPI
from app.core.database import engine, Base

from app.routes import student, grade, ai
from app.routes import exam
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="School AI Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(student.router)
app.include_router(grade.router)
app.include_router(ai.router)
app.include_router(exam.router)

@app.get("/")
def root():
    return {"message": "API rodando 🚀"}