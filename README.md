
# AI Resume Analyzer

An AI-powered Resume Analyzer that compares a candidate's resume against a Job Description (JD), identifies skill gaps, calculates an indicative ATS match score, and generates AI-powered resume improvement suggestions.

## Project Objective

The objective of this project is to build a GenAI-powered application that helps candidates understand how well their resumes align with a target job description.

## Features

- Upload resume in PDF format.
- Paste a Job Description.
- Extract resume text using PyPDF.
- Extract candidate skills and experience using Groq LLM.
- Identify required and missing skills.
- Analyze candidate experience against job requirements.
- Generate an indicative ATS match score.
- Generate semantic embeddings using Sentence Transformers.
- Perform similarity search using FAISS.
- Generate AI-powered resume improvement suggestions.
- Display and download the final analysis report.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| LLM | Groq |
| LLM Integration | LangChain |
| PDF Extraction | PyPDF |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| Vector Database | FAISS |
| Embedding Library | Sentence Transformers |
| Configuration | Python-dotenv |


## Application Architecture

1. Streamlit accepts the resume PDF and job description.
2. PyPDF extracts resume text.
3. Groq + LangChain extracts candidate skills, experience, and job requirements.
4. Python performs skill matching and experience analysis.
5. Sentence Transformers generates embeddings for resume chunks.
6. FAISS retrieves the top 5 relevant resume sections.
7. Python calculates the indicative ATS score.
8. Groq + LangChain generates recommendations using the full resume, job description, analysis results, and retrieved sections.
9. Streamlit displays the results and downloadable report.


## System Architecture
![AI Resume Analyzer Architecture](docs/architecture.png)


## Project Structure

ai-resume-analyzer/
│
├── src/
│   ├── resumeparser.py
│   ├── jd_parser.py
│   ├── skill_extractor.py
│   ├── skill_matcher.py
│   ├── experience_analyser.py
│   ├── ats_scorer.py
│   ├── recommendation.py
│   ├── report_generator.py
│   ├── vector_store.py
│   └── workflow.py
│
├── tests/
│   ├── test_ats_scorer.py
│   ├── test_embeddings.py
│   ├── test_experience_analyser.py
│   ├── test_recommendation.py
│   ├── test_skill_extractor.py
│   ├── test_skill_matched.py
│   ├── test_vector_store.py
│   └── test_workflow.py
│
├── docs/
│   └── architecture.png
│
├── app.py
├── README.md
├── requirements.txt
├── requirements-lock.txt
├── .env.example
└── .gitignore


## Setup Instructions

### 1. Clone the repository

git clone https://github.com/kiran-kumar-aidev/ai-resume-analyzer.git

cd ai-resume-analyzer

### 2. Create a virtual environment

python -m venv venv

### 3. Activate the environment

Windows PowerShell:

.\venv\Scripts\Activate.ps1

### 4. Install dependencies

pip install -r requirements.txt

### 5. Configure Groq API Key

Create a `.env` file in the project root.

GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b

### 6. Run the application

streamlit run app.py

## ATS Scoring Methodology

The project uses a configurable weighted scoring formula:

| Parameter | Weight |
|---|---:|
| Required Skills Match | 40% |
| Experience Match | 30% |
| Education Match | 10% |
| Responsibility Match | 20% |

The resulting score is an indicative project-level match score. It is not an actual employer ATS score.

## How It Works

1. Candidate uploads a resume PDF.
2. Candidate provides the target Job Description.
3. PyPDF extracts resume content.
4. Groq LLM extracts candidate skills, experience, and JD requirements.
5. Python compares candidate skills with required skills.
6. Experience analyzer checks the experience requirement.
7. ATS scoring module calculates the weighted match score.
8. Sentence Transformers generates resume text embeddings.
9. FAISS retrieves semantically relevant resume sections.
10. Groq generates resume improvement recommendations.
11. Streamlit displays the analysis and provides a downloadable report.
