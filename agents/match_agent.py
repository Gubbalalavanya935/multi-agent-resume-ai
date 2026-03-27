import re

# Calculate match score, strengths, weaknesses
def calculate_score(job_skills, resume_text, threshold=70):

    resume_text = resume_text.lower()

    matched = []
    for skill in job_skills:
        if skill.lower() in resume_text:
            matched.append(skill)

    missing = list(set(job_skills) - set(matched))
    score = (len(matched) / len(job_skills)) * 100 if job_skills else 0

    # Suggestions (basic)
    suggestions = [f"Improve {skill}" for skill in missing]

    # Decision based on score
    decision = "Shortlist" if score >= threshold else "Not Shortlisted"

    result = {
        "score": round(score, 2),
        "strengths": matched,
        "weakness": missing,
        "suggestions": suggestions,
        "decision": decision
    }

    return result


# Main function for matching resume
def match_resume(resume_data, job_skills, threshold=70):

    job_skills_list = [s.strip().lower() for s in job_skills.split(",")]

    return calculate_score(job_skills_list, resume_data, threshold)