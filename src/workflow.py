from src.resumeparser import extract_resume_text
from src.jd_parser import extract_jd_text
from src.skill_extractor import extract_skills, llm
from src.skill_matcher import compare_skills
from src.experience_analyser import analyze_experience
from src.ats_scorer import calculate_ats_score
from src.recommendation import generate_recommendations
from src.report_generator import generator_final_report
from src.vector_store import (
    create_vector_store,
    search_similar_texts
)

def analyze_resume(pdf_file, jd_input):
    resume_text = extract_resume_text(pdf_file)

    jd_text = extract_jd_text(jd_input)

    resume_chunks = [
       chunk.strip()
       for chunk in resume_text.split("\n")
       if len(chunk.strip()) > 30
    ]

    vector_index = create_vector_store(resume_chunks)

    relevant_resume_sections = search_similar_texts(
        vector_index,
        jd_text,
        resume_chunks,
        top_k=5
    )

    extracted_data = extract_skills(
        resume_text,
        jd_text
    )

    skill_analysis = compare_skills(
        extracted_data["candidate_skills"],
        extracted_data["required_skills"],
        extracted_data["preferred_skills"]
    )

    experience_analysis = analyze_experience(
        extracted_data["candidate_experience_years"],
        extracted_data["required_experience_years"]
    )

    ats_score = calculate_ats_score(
        skill_match_percentage=skill_analysis[
            "required_skill_match_percentage"
        ],
        experience_score=experience_analysis["experience_score"]
    )

    recommendation = generate_recommendations(
        llm=llm,
        resume_text=resume_text,
        jd_text=jd_text,
        matched_skills=skill_analysis["matched_skills"],
        missing_skills=skill_analysis["missing_skills"],
        relevant_resume_sections=relevant_resume_sections
    )

    report = generator_final_report(
        ats_score=ats_score,
        matched_skills=skill_analysis["matched_skills"],
        missing_skills=skill_analysis["missing_skills"],
        experience_analysis=experience_analysis,
        recommendations=recommendation
    )

    return {
        "extracted_data": extracted_data,
        "skill_analysis": skill_analysis,
        "experience_analysis": experience_analysis,
        "ats_score": ats_score,
        "recommendations": recommendation,
        "report": report,
        "relevant_resume_sections": relevant_resume_sections
    }



