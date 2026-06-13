from modules.roadmap_generator import generate_roadmap
from modules.skill_gap import get_skill_gap
from modules.skill_extractor import extract_skills
from modules.pdf_parser import extract_text_from_pdf
import streamlit as st

st.set_page_config(
    page_title="CareerGPT",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CareerGPT")
st.subheader("AI Career Mentor & Internship Readiness Platform")

st.write(
    "Upload your resume, identify skill gaps, generate learning roadmaps and prepare for internships."
)

st.divider()

role = st.selectbox(
    "Select Your Target Career Role",
    [
        "AI Engineer",
        "Data Scientist",
        "Machine Learning Engineer",
        "Frontend Developer",
        "Backend Developer",
        "Cybersecurity Analyst"
    ]
)

st.write("Selected Role:", role)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)
    skills = extract_skills(resume_text)
    required_skills, missing_skills = get_skill_gap(
    role,
    skills
)

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )
    st.subheader("Detected Skills")

    for skill in skills:
        st.write("✅", skill)
    st.subheader("Required Skills For Role")

    for skill in required_skills:
        st.write("🎯", skill)
    st.subheader("Skill Gap Analysis")
    

    if len(missing_skills) == 0:

        st.success(
            "You already possess all required skills!"
        )

    else:

        st.warning(
            f"You need {len(missing_skills)} additional skills."
        )
        for skill in missing_skills:
            st.write("❌", skill)
    st.divider()

    if st.button("Generate Career Roadmap"):

        roadmap = generate_roadmap(
            role,
            missing_skills
        )

        st.subheader("Career Roadmap")

        st.text_area(
            "Roadmap",
            roadmap,
            height=300
        )
        