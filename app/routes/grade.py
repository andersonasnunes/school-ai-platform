from fastapi import APIRouter
from app.services.grade_service import calculate_final_grade

router = APIRouter(prefix="/grades")

@router.post("/calculate")
def calculate(data: dict):
    result = calculate_final_grade(
        data["evaluations"],
        data["extra_points"]
    )
    return {"final_grade": result}