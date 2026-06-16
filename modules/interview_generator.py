from modules.llm_service import generate_response


def generate_interview_questions(
    role,
    skills,
    missing_skills,
    resume_text
):

    prompt = f"""
You are an expert technical interviewer.

Candidate Resume:
{resume_text}

Target Role:
{role}

Detected Skills:
{skills}

Missing Skills:
{missing_skills}

Generate:

1. 10 Technical Interview Questions
2. 5 Project-Based Questions
3. 5 HR Questions

The questions must be personalized according to the resume.

Do not give answers.

Format clearly.
"""

    return generate_response(prompt)