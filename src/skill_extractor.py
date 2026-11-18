import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    model_name = os.getenv("GROQ_MODEL"),
    temperature=0,
    api_key = os.getenv("GROQ_API_KEY")

)


prompt = ChatPromptTemplate.from_template("""
You are a resume information extraction system.

Read both inputs carefully and extract information that is explicitly present.

RESUME TEXT:
{resume_text}

JOB DESCRIPTION TEXT:
{jd_text}

Return a JSON object with these fields:

{{
    "candidate_skills": ["Python", "SQL"],
    "candidate_experience_years": 5,
    "required_skills": ["Python", "LangChain"],
    "preferred_skills": ["FAISS"],
    "required_experience_years": 4,
    "relevant_responsibilities": ["Building AI applications"]
}}

Extraction instructions:

1. Extract every technical skill explicitly mentioned in the resume.
2. Extract required skills explicitly mentioned in the job description.
3. Extract preferred skills separately.
4. Extract candidate experience from the resume.
5. Extract required experience from the job description.
6. Extract responsibilities from the job description.
7. Do not return empty arrays when relevant information exists in the input.
8. Use null only when experience information is unavailable.
9. Return only valid JSON. Do not return Markdown.

The example values above are illustrative. Do not copy them unless they appear in the inputs.
""")


def extract_skills(resume_text, jd_text):
    messages = prompt.format_messages(
        resume_text=resume_text,
        jd_text=jd_text
    )

    response = llm.invoke(messages)

    print("\nRAW GROQ RESPONSE:")
    print(response.content)

    return json.loads(response.content)