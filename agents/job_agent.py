from data.job_skills import JOB_SKILLS

def research_job(job_role):

    role = job_role.lower()

    if role in JOB_SKILLS:
        return ", ".join(JOB_SKILLS[role])

    return ""