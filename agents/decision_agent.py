from config import client

def hiring_decision(match_result):

    prompt = f"""
    Based on this match analysis decide:

    Shortlist or Reject candidate.

    Analysis:
    {match_result}
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content