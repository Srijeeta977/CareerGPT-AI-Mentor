def generate_roadmap(role, missing_skills):

    roadmap = f"""
Target Role: {role}

Missing Skills:
{', '.join(missing_skills)}

Learning Plan:
"""

    for i, skill in enumerate(missing_skills, start=1):

        roadmap += f"\nWeek {i}: Learn {skill}"

    return roadmap