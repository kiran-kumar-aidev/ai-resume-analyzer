
from src.skill_extractor import llm
from src.recommendation import generate_recommendations

resume_text = """
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
Responsibilities:
- Build and maintain RAG pipelines.
- Develop multi-agent AI workflows.
"""

result = generate_recommendations(
    llm=llm,
    resume_text=resume_text,
    jd_text=jd_text,
    matched_skills=["Python", "LangChain", "RAG"],
    missing_skills=["FAISS", "LangGraph"]
)

print("\nAI Recommendations:")
print(result)
