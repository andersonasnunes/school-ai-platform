from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.core.database import Base

class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    name = Column(String)
    score = Column(Float)
    weight = Column(Float)