from sqlalchemy import Column, Integer, Float, ForeignKey
from app.core.database import Base

class ExtraPoint(Base):
    __tablename__ = "extra_points"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    value = Column(Float)