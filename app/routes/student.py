from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.student import Student

router = APIRouter(prefix="/students")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_student(name: str, db: Session = Depends(get_db)):
    student = Student(name=name)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@router.get("/")
def list_students(db: Session = Depends(get_db)):
    return db.query(Student).all()