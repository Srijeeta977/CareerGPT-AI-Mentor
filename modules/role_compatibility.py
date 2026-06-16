def calculate_role_compatibility(
    skills,
    required_skills
):

    matched = 0

    skills_lower = [
        skill.lower().strip()
        for skill in skills
    ]

    for skill in required_skills:

        if skill.lower().strip() in skills_lower:
            matched += 1

    score = (
        matched / len(required_skills)
    ) * 100

    return round(score)