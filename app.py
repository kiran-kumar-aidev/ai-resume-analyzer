
import streamlit as st

from src.workflow import analyze_resume


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.caption(
    "AI-powered resume analysis and job description matching"
)

st.divider()

# -----------------------------
# INPUT SECTION
# -----------------------------

st.subheader("1. Upload Resume")

resume_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)

st.subheader("2. Job Description")

jd_text = st.text_area(
    "Paste the Job Description",
    height=220,
    placeholder="Paste the complete job description here..."
)

analyze_button = st.button(
    "Analyze Resume",
    type="primary",
    use_container_width=True
)


# -----------------------------
# ANALYSIS
# -----------------------------

if analyze_button:

    if resume_file is None:
        st.error("Please upload a resume PDF.")

    elif not jd_text.strip():
        st.error("Please enter a Job Description.")

    else:
        with st.spinner("Analyzing your resume..."):

            try:
                result = analyze_resume(
                    resume_file,
                    jd_text
                )

                st.session_state["analysis_result"] = result

            except Exception as e:
                st.error(f"Analysis failed: {e}")


# -----------------------------
# RESULTS SECTION
# -----------------------------

if "analysis_result" in st.session_state:

    result = st.session_state["analysis_result"]

    skill_analysis = result["skill_analysis"]
    experience = result["experience_analysis"]

    st.divider()
    st.header("3. Resume Analysis Results")

    # ATS score and summary metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "ATS Match Score",
            f'{result["ats_score"]}%'
        )

    with col2:
        st.metric(
            "Matched Skills",
            len(skill_analysis["matched_skills"])
        )

    with col3:
        st.metric(
            "Missing Skills",
            len(skill_analysis["missing_skills"])
        )

    st.caption(
        "Indicative project score based on the configured "
        "weighted matching formula. Not an actual employer ATS score."
    )

    st.divider()

    # Skills
    st.subheader("4. Skills Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### ✅ Matched Skills")

        if skill_analysis["matched_skills"]:
            for skill in skill_analysis["matched_skills"]:
                st.success(skill)
        else:
            st.info("No matched skills found.")

    with col2:
        st.markdown("#### ⚠️ Missing Required Skills")

        if skill_analysis["missing_skills"]:
            for skill in skill_analysis["missing_skills"]:
                st.warning(skill)
        else:
            st.success("No missing required skills.")

    st.divider()

    # Experience
    st.subheader("5. Experience Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Candidate Experience",
            f'{result["extracted_data"]["candidate_experience_years"]} years'
            if result["extracted_data"]["candidate_experience_years"] is not None
            else "Not available"
        )

    with col2:
        st.metric(
            "Required Experience",
            f'{result["extracted_data"]["required_experience_years"]} years'
            if result["extracted_data"]["required_experience_years"] is not None
            else "Not available"
        )

    st.write("**Status:**", experience["experience_status"])

    st.divider()

    # FAISS Retrieval Results
    st.subheader("6. Relevant Resume Sections (FAISS Retrieval)")

    retrieved_sections = result["relevant_resume_sections"]

    if retrieved_sections:

        for index, item in enumerate(retrieved_sections, start=1):

            with st.expander(
                f"Retrieved Section {index} | Similarity: {item['similarity_score']}"
            ):
                st.write(item["text"])

    else:
        st.info("No relevant resume sections retrieved.")

    st.divider()

    # AI Recommendations
    st.subheader("7. Resume Improvement Suggestions")

    st.markdown(result["recommendations"])

    st.divider()

    # Final report
    st.subheader("8. Final Analysis Report")

    with st.expander("View complete report", expanded=False):
        st.text(result["report"])

    st.download_button(
        label="📥 Download Analysis Report",
        data=result["report"],
        file_name="resume_analysis_report.txt",
        mime="text/plain",
        use_container_width=True
    )
