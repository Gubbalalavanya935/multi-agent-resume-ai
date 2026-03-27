from config import client

def analyze_resume(resume_text):

    prompt = f"""
    Extract the following from the resume:

    Name
    Skills
    Experience
    Education

    Resume:
    {resume_text}
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content
