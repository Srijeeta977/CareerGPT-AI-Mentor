from modules.llm_service import generate_response
import ast


def extract_skills_ai(resume_text):

    prompt = f"""
Extract ONLY technical skills from this resume.

Include:
- Programming Languages
- Frameworks
- Libraries
- Databases
- Cloud Platforms
- AI/ML Technologies
- Cybersecurity Tools
- Developer Tools

Return ONLY a Python list.

Resume:
{resume_text}
"""

    response = generate_response(prompt)

    try:
        skills = ast.literal_eval(response)

        cleaned_skills = []

        for skill in skills:

            skill = str(skill).strip()

            if skill and skill not in cleaned_skills:
                cleaned_skills.append(skill)

        return cleaned_skills

    except:
        return []