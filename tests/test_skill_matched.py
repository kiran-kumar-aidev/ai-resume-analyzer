from src.skill_matcher import compare_skills

candidate_skill = [
    "Python",
    "SQL",
    "Machine Learning",
    "LangChain",
    "RAG"
]

required_skills = [
    "Python",
    "LangChain",
    "RAG",
    "FAISS",
    "LangGraph"
]

preferred_skills = ["Docker", "AWS"]

result = compare_skills(
    candidate_skill,
    required_skills,
    preferred_skills
)

print("\nSkill Comparision Result:")
print(result)