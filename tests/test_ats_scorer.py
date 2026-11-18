from src.ats_scorer import calculate_ats_score

score = calculate_ats_score(
    skill_match_percentage=60,
    experience_match=True,
    education_match=100,
    responsibility_match=0
)

print("ATS Match Score: ", score)