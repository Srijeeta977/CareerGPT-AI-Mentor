from modules.llm_service import generate_response

def generate_roadmap(
    role,
    skills,
    missing_skills,
    resume_text
):

    prompt = f"""
You are an expert career mentor.

Resume Content:
{resume_text}

Detected Skills:
{', '.join(skills)}

Target Role:
{role}

Missing Skills:
{', '.join(missing_skills)}

Generate a personalized career roadmap.

Include:

1. Summary of current profile
2. Strengths identified from resume
3. Missing skills to focus on
4. Week-by-week learning roadmap
5. Recommended projects
6. Interview preparation tips

Keep the roadmap practical for a college student.
"""

    return generate_response(prompt)