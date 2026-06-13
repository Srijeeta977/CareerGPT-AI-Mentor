import pandas as pd


def get_skill_gap(selected_role, user_skills):

    roles_df = pd.read_csv("data/roles.csv")

    role_row = roles_df[
        roles_df["Role"] == selected_role
    ]

    if role_row.empty:
        return [], []

    required_skills = role_row.iloc[0]["Skills"]

    required_skills = [
        skill.strip()
        for skill in required_skills.split(",")
    ]

    missing_skills = []

    for skill in required_skills:

        if skill not in user_skills:
            missing_skills.append(skill)

    return required_skills, missing_skills