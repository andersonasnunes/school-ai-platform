# app/schemas/lesson.py

from pydantic import BaseModel

class LessonRequest(BaseModel):
    subject: str
    grade: str
    level: str
    topic: str
    subtopics: str