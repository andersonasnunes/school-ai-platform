# app/services/grade_service.py

def calculate_final_grade(evaluations, extra_points):
    total = 0
    total_weight = 0

    for ev in evaluations:
        total += ev["score"] * ev["weight"]
        total_weight += ev["weight"]

    base_average = total / total_weight if total_weight > 0 else 0

    extra = sum(p["value"] for p in extra_points)

    final = base_average + extra

    return round(final, 2)