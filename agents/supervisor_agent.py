from agents.resume_agent import analyze_resume
from agents.job_agent import research_job
from agents.jd_agent import extract_jd_skills
from agents.match_agent import match_resume

def run_pipeline(resume_text, job_role=None, job_description=None):

    resume_data = analyze_resume(resume_text)

    # Job Role or JD
    if job_role:
        job_skills = research_job(job_role)
    elif job_description:
        job_skills = extract_jd_skills(job_description)
    else:
        job_skills = ""

    # Match resume
    match_result = match_resume(resume_data, job_skills)

    # Human-readable summary
    summary_text = f"""
Score: {match_result['score']}%

Strengths: {', '.join(match_result['strengths']) if match_result['strengths'] else 'None'}

Weakness: {', '.join(match_result['weakness']) if match_result['weakness'] else 'None'}

Suggestions: {', '.join(match_result['suggestions']) if match_result['suggestions'] else 'None'}

Decision: {match_result['decision']}
"""

    return {
        "resume": resume_data,
        "job": job_skills,
        "match": summary_text,
        "decision": match_result["decision"]
    }