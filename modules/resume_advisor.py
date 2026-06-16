from modules.llm_service import generate_response

def analyze_resume(resume_text):

    prompt = f"""
You are an expert ATS Resume Reviewer and Career Mentor.

Analyze the following resume.

Resume:
{resume_text}

Give the output in the following format:

Strengths:
- point 1
- point 2
- point 3

Weaknesses:
- point 1
- point 2
- point 3

ATS Improvement Suggestions:
- point 1
- point 2
- point 3

Recommended Projects:
- project 1
- project 2
- project 3

Keep feedback practical and student-friendly.
"""

    return generate_response(prompt)