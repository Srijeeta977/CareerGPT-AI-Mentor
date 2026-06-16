from modules.llm_service import generate_response


def generate_learning_resources(
    role,
    missing_skills
):

    prompt = f"""
You are a career mentor.

Target Role:
{role}

Missing Skills:
{missing_skills}

Suggest:

1. Best Free Courses
2. Best YouTube Channels
3. Best Practice Platforms
4. Certifications
5. Learning Order

Keep recommendations practical for college students.

Format clearly.
"""

    return generate_response(prompt)