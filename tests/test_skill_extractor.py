from src.skill_extractor import extract_skills

resume_text="""
Python Developer with 5 years of experience.
Skills: Python, SQL, Machine Learning, LangChain, RAG.
Experience building AI-powered applications.
"""

jd_text = """
We are looking for an AI Engineer with:
- Python
- LangChain
- RAG
- FAISS
- LangGraph

Required experience: 4 years.
"""

result = extract_skills(resume_text, jd_text)

print("\nSkill Extraction Result: ")
print(result)