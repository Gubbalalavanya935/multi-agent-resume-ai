from config import client

def extract_jd_skills(job_description):

    prompt = f"""
Extract ONLY technical skills from this job description.

Return skills separated by commas.

Example:
python, django, sql, docker

Job Description:
{job_description}
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0,
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content