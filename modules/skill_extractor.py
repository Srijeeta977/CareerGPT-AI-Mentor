import pandas as pd


def extract_skills(resume_text):

    skills_df = pd.read_csv("data/skills.csv")

    skills_list = skills_df["Skill"].tolist()

    found_skills = []

    resume_text = resume_text.lower()

    for skill in skills_list:

        if skill.lower() in resume_text:

            found_skills.append(skill)

    return sorted(list(set(found_skills)))