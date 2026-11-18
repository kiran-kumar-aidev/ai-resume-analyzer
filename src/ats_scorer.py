
def calculate_ats_score(
    skill_match_percentage,
    experience_score,
    education_match=100,
    responsibility_match=0
):
    weights = {
        "skills": 0.40,
        "experience": 0.30,
        "education": 0.10,
        "responsibilities": 0.20
    }

    final_score = (
        skill_match_percentage * weights["skills"]
        + experience_score * weights["experience"]
        + education_match * weights["education"]
        + responsibility_match * weights["responsibilities"]
    )

    return round(final_score, 2)
