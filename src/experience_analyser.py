
def analyze_experience(
    candidate_experience,
    required_experience
):
    if candidate_experience is None or required_experience is None:
        return {
            "experience_match": False,
            "experience_gap": None,
            "experience_status": "Experience information unavailable",
            "experience_score": 0
        }

    experience_gap = round(
        candidate_experience - required_experience, 2
    )

    experience_score = min(
        (candidate_experience / required_experience) * 100,
        100
    ) if required_experience > 0 else 100

    return {
        "experience_match": experience_gap >= 0,
        "experience_gap": experience_gap,
        "experience_status": (
            "Meets requirement"
            if experience_gap >= 0
            else "Below requirement"
        ),
        "experience_score": round(experience_score, 2)
    }
