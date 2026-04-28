# app/routes/exam.py

from fastapi import APIRouter
from app.ai.exam_generator import generate_exam
from app.schemas.exam import ExamRequest

router = APIRouter(prefix="/exam", tags=["Exam"])

@router.post("/")
def create_exam(data: ExamRequest):
    return {"exam": generate_exam(data.dict())}