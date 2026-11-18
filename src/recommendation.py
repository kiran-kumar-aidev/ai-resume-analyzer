
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    """
You are an expert resume reviewer.

Analyze the candidate's resume against the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{jd_text}

MATCHED SKILLS:
{matched_skills}

MISSING SKILLS:
{missing_skills}

RELEVANT RESUME SECTIONS RETRIEVED USING FAISS:
{relevant_resume_sections}

Use the relevant resume sections as additional context.
Base your recommendations only on information supported by the resume.
If a relevant section does not provide enough evidence, do not make assumptions.

Provide recommendations in these three sections:

1. Resume Improvements
- Suggest specific improvements to the resume.
- Focus on relevance to the job description.

2. Missing Skills
- Explain which missing skills the candidate should consider learning.
- Do not claim the candidate has skills that are absent from the resume.

3. Content Improvements
- Suggest improvements to resume bullet points.
- Never invent projects, experience, achievements, or metrics.

Keep the recommendations practical and concise.
"""
)


def generate_recommendations(
    llm,
    resume_text,
    jd_text,
    matched_skills,
    missing_skills,
    relevant_resume_sections
):
    retrieved_context = "\n\n".join(
        item["text"] for item in relevant_resume_sections
    )

    messages = prompt.format_messages(
        resume_text=resume_text,
        jd_text=jd_text,
        matched_skills=", ".join(matched_skills),
        missing_skills=", ".join(missing_skills),
        relevant_resume_sections=retrieved_context
    )

    response = llm.invoke(messages)
    return response.content
