# app/routes/ai.py

from fastapi import APIRouter
from app.ai.tutor import generate_lesson
from app.schemas.lesson import LessonRequest

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/lesson")
def generate(data: LessonRequest):
    content = generate_lesson(data.dict())
    return {"lesson": content}