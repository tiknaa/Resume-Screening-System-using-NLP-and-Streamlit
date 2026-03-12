import streamlit as st

from parser import extract_text_from_pdf
from nlp_utils import preprocess
from matcher import similarity
from skills import extract_skills


st.title("AI Resume Screening System")

st.write("Upload resumes and compare with job description")


resumes = st.file_uploader(
    "Upload Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

job_description = st.text_area("Paste Job Description")


if st.button("Evaluate Candidates"):

    if resumes and job_description:

        jd_clean = preprocess(job_description)

        results = []

        for file in resumes:

            resume_text = extract_text_from_pdf(file)

            resume_clean = preprocess(resume_text)

            score = similarity(resume_clean, jd_clean)

            skills = extract_skills(resume_clean)

            results.append((file.name, score, skills))

        results = sorted(results, key=lambda x: x[1], reverse=True)

        for name, score, skills in results:

            st.write("Candidate:", name)

            st.write("Match Score:", round(score*100,2), "%")

            st.write("Skills:", skills)

            st.write("---")