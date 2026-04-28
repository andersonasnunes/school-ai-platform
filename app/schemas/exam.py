# app/schemas/exam.py

from pydantic import BaseModel

class ExamRequest(BaseModel):
    subject: str
    grade: str
    level: str
    topic: str
    subtopics: str
    difficulty: str
    questions: int