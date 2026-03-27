import streamlit as st
import json
import re

from tools.pdf_reader import read_pdf
from agents.supervisor_agent import run_pipeline
from memory.save_memory import save_candidate
from tools.pdf_report import create_report

st.set_page_config(page_title="Agentic AI Resume Analyzer", layout="wide")

st.title("🤖 Agentic AI Resume Analyzer")


# Upload resumes
uploaded_files = st.file_uploader(
    "Upload Resumes (PDF)",
    accept_multiple_files=True
)


# Choose input type
mode = st.radio(
    "Select Input Method",
    ["Job Role", "Job Description"]
)

job_role = None
job_description = None


# Option 1: Job Role
if mode == "Job Role":

    job_role = st.selectbox(
        "Select Job Role",
        [
            "Python Developer",
            "Data Scientist",
            "Machine Learning Engineer",
            "AI Engineer",
            "Backend Developer",
            "Frontend Developer",
            "Full Stack Developer",
            "DevOps Engineer",
            "Cloud Engineer",
            "Software Engineer"
        ]
    )

    job_role = job_role.lower()


# Option 2: Job Description
else:

    job_description = st.text_area(
        "Paste Job Description",
        height=200
    )


# Extract percentage score safely
def extract_score(match_text):

    match = re.search(r"(\d+\.?\d*)%", match_text)

    return float(match.group(1)) if match else 0


# Analyze button
if st.button("Analyze Candidates"):

    if not uploaded_files:
        st.warning("Please upload at least one resume.")
        st.stop()

    if mode == "Job Description" and not job_description:
        st.warning("Please paste a job description.")
        st.stop()

    candidates = []

    for file in uploaded_files:

        st.divider()
        st.subheader(f"📄 Processing: {file.name}")

        # Read resume
        resume_text = read_pdf(file)

        # Run AI pipeline
        result = run_pipeline(
            resume_text,
            job_role=job_role,
            job_description=job_description
        )

        # Display results
        st.write("### Resume Analysis")
        st.write(result["resume"])

        st.write("### Job Skills")
        st.write(result["job"])

        st.write("### Match Result")
        st.write(result["match"])

        st.write("### Final Decision")
        st.write(result["decision"])

        # Save candidate to memory
        save_candidate({
            "candidate": file.name,
            "job_role": job_role if job_role else "JD Based",
            "result": result
        })

        # Generate PDF report
        report_file = create_report(result)

        with open(report_file, "rb") as f:
            st.download_button(
                label=f"Download Report for {file.name}",
                data=f,
                file_name=f"{file.name}_report.pdf",
                mime="application/pdf"
            )

        # Store score for ranking
        candidates.append({
            "name": file.name,
            "score": extract_score(result["match"])
        })


    # Candidate Ranking
    ranking = sorted(
        candidates,
        key=lambda x: x["score"],
        reverse=True
    )

    st.divider()
    st.header("🏆 Candidate Ranking")

    for i, c in enumerate(ranking):
        st.write(f"{i+1}. {c['name']} — {c['score']}%")


# Dashboard Section
st.divider()
st.header("📊 HR Analytics Dashboard")

try:

    with open("memory/history.json") as f:
        data = json.load(f)

    total_candidates = len(data)

    scores = []
    shortlisted = 0

    for c in data:

        text = c["result"]["match"]

        match = re.search(r"(\d+\.?\d*)%", text)

        if match:
            scores.append(float(match.group(1)))

        if "Shortlist" in c["result"]["decision"]:
            shortlisted += 1

    avg_score = sum(scores) / len(scores) if scores else 0

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Candidates", total_candidates)
    col2.metric("Average Match Score", round(avg_score, 2))
    col3.metric("Shortlisted Candidates", shortlisted)

except:
    st.info("No candidate data yet. Upload resumes to generate analytics.")