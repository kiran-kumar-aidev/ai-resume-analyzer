def extract_jd_text(jd_text):
    if not jd_text or not jd_text.strip():
        raise ValueError("Job Description cannot be empty.")
    return jd_text.strip()