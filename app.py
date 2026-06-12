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