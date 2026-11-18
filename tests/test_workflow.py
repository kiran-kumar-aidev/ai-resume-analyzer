
from src.workflow import analyze_resume

resume_path = "data/sample_resume.pdf"

jd_text = """
We are looking for an AI Engineer.

Required skills:
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

with open(resume_path, "rb") as resume_file:
    result = analyze_resume(resume_file, jd_text)

print(result["report"])

print("\nFAISS RETRIEVED RESUME SECTIONS:")

for item in result["relevant_resume_sections"]:
    print("\nText:", item["text"])
    print("Similarity:", item["similarity_score"])