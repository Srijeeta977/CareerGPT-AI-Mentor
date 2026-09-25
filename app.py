from modules.role_compatibility import calculate_role_compatibility
from modules.resource_generator import generate_learning_resources
from modules.interview_generator import generate_interview_questions
from modules.resume_advisor import analyze_resume
from modules.roadmap_generator import generate_roadmap
from modules.skill_gap import get_skill_gap
from modules.ai_skill_extractor import extract_skills_ai
from modules.pdf_parser import extract_text_from_pdf
import streamlit as st

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(
135deg,
#0f172a,
#111827,
#1e293b
);
}

.main{
padding-top:1rem;
}

h1{
color:#ffffff;
font-weight:700;
}

h2,h3{
color:#f8fafc;
}

.stMetric{
background:rgba(255,255,255,0.05);
padding:20px;
border-radius:18px;
border:1px solid rgba(255,255,255,0.1);
box-shadow:0 4px 20px rgba(0,0,0,0.3);
}

.stTextArea textarea{
border-radius:12px;
}

.stButton>button{
width:100%;
height:50px;
border-radius:12px;
font-weight:bold;
background:linear-gradient(
90deg,
#3b82f6,
#8b5cf6
);
color:white;
border:none;
}

.stButton>button:hover{
transform:scale(1.02);
}

[data-testid="stSidebar"]{
background:#111827;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="CareerGPT",
    page_icon="🚀",
    layout="wide"
)
st.sidebar.title("🚀 CareerGPT")
st.markdown("""
### AI-Powered Career Intelligence Platform

Analyze resumes • Discover skill gaps • Generate roadmaps • Prepare for interviews

---
""")

st.sidebar.image(
"https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
width=120
)

st.sidebar.title("CareerGPT")

st.sidebar.markdown("""
### 🚀 Platform Features

✅ Resume Analysis

✅ Role Compatibility

✅ Skill Gap Detection

✅ AI Roadmaps

✅ Interview Preparation

✅ Learning Resources
""")

st.sidebar.markdown("---")

st.sidebar.info(
"Built for students, freshers and internship seekers."
)

st.title("🚀 CareerGPT")
st.subheader("AI Career Mentor & Internship Readiness Platform")

st.write(
    "Upload your resume, identify skill gaps, generate learning roadmaps and prepare for internships."
)

st.divider()

st.markdown("""
<div style="
padding:20px;
border-radius:15px;
background:linear-gradient(
90deg,
#2563eb,
#7c3aed
);
color:white;
margin-bottom:20px;
">

<h2>🚀 Career Readiness Starts Here</h2>

Upload your resume and discover:

✔ Role Compatibility

✔ Missing Skills

✔ AI Roadmaps

✔ Interview Questions

✔ Learning Resources

</div>
""", unsafe_allow_html=True)

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

st.info(f"🎯 Target Role: {role}")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)
    skills = extract_skills_ai(resume_text)
    required_skills, missing_skills = get_skill_gap(
    role,
    skills
)
    compatibility_score = calculate_role_compatibility(
        skills,
        required_skills
)
    if compatibility_score >= 80:
        st.success("Excellent match for this role.")
    elif compatibility_score >= 60:
        st.info("Good match. Improve a few missing skills.")
    elif compatibility_score >= 40:
        st.warning("Moderate match. Upskilling recommended.")
    else:
        st.error("Low match. Significant skill development required.")

    with st.expander("📄 View Extracted Resume Text"):
        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎯 Role Compatibility",
            f"{compatibility_score}%"
        )

    with col2:
        st.metric(
            "❌ Missing Skills",
            len(missing_skills)
        )
    with col3:
        st.metric(
            "✅ Matched Skills",
            len(required_skills)-len(missing_skills)
        )

    st.subheader("🛠 Detected Technical Skills")

    col1, col2, col3 = st.columns(3)

    for i, skill in enumerate(skills):

        if i % 3 == 0:
            col1.success(f"✅ {skill}")

        elif i % 3 == 1:
            col2.success(f"✅ {skill}")

        else:
            col3.success(f"✅ {skill}")
        
    
    st.subheader(f"🎯 Skills Required For {role}")

    required_text = ""

    for skill in required_skills:
        required_text += f"🎯 {skill}\n"

    st.text_area(
        "Required Skills",
        required_text,
        height=150
    )
    st.subheader("📊 Skill Gap Analysis")

    if len(missing_skills) == 0:

        st.success(
            "✅ Your resume already matches all required skills for this role."
        )

    else:

        st.warning(
            f"You need {len(missing_skills)} additional skill(s) for this role."
        )

        missing_text = ""

        for skill in missing_skills:
            missing_text += f"❌ {skill}\n"

        st.text_area(
            "Missing Skills",
            missing_text,
            height=150
        )
        st.divider()

        tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📄 Resume Advisor",
            "🛣 Career Roadmap",
            "🎤 Interview Questions",
            "📚 Learning Resources"
        ]
    )

    # Create session state for AI results
    if "resume_advice" not in st.session_state:
        st.session_state.resume_advice = None

    if "career_roadmap" not in st.session_state:
        st.session_state.career_roadmap = None

    if "interview_questions" not in st.session_state:
        st.session_state.interview_questions = None

    if "learning_resources" not in st.session_state:
        st.session_state.learning_resources = None


    # -----------------------------
    # Resume Advisor
    # -----------------------------

    with tab1:

        st.subheader("📄 AI Resume Advisor")

        st.write(
            "Get AI-powered feedback based on your uploaded resume."
        )

        if st.button("✨ Analyze My Resume", key="resume_advisor_btn"):

            with st.spinner("Analyzing your resume..."):

                try:

                    st.session_state.resume_advice = analyze_resume(
                        resume_text
                    )

                except Exception as e:

                    st.session_state.resume_advice = (
                        f"⚠️ AI service error:\n\n{str(e)}"
                    )

        if st.session_state.resume_advice:

            st.markdown("### 📊 Resume Analysis")

            st.markdown(
                st.session_state.resume_advice
            )


    # -----------------------------
    # Career Roadmap
    # -----------------------------

    with tab2:

        st.subheader("🛣 Personalized Career Roadmap")

        st.write(
            "Generate a roadmap based on your resume, target role and skill gaps."
        )

        if st.button("🚀 Generate Career Roadmap", key="roadmap_btn"):

            with st.spinner("Creating your personalized roadmap..."):

                try:

                    st.session_state.career_roadmap = generate_roadmap(
                        role,
                        skills,
                        missing_skills,
                        resume_text
                    )

                except Exception as e:

                    st.session_state.career_roadmap = (
                        f"⚠️ AI service error:\n\n{str(e)}"
                    )

        if st.session_state.career_roadmap:

            st.markdown("### 🗺 Your Roadmap")

            st.markdown(
                st.session_state.career_roadmap
            )


    # -----------------------------
    # Interview Questions
    # -----------------------------

    with tab3:

        st.subheader("🎤 AI Interview Preparation")

        st.write(
            "Generate interview questions specifically based on your resume and target role."
        )

        if st.button(
            "🎯 Generate Interview Questions",
            key="interview_btn"
        ):

            with st.spinner("Generating personalized interview questions..."):

                try:

                    st.session_state.interview_questions = (
                        generate_interview_questions(
                            role,
                            skills,
                            missing_skills,
                            resume_text
                        )
                    )

                except Exception as e:

                    st.session_state.interview_questions = (
                        f"⚠️ AI service error:\n\n{str(e)}"
                    )

        if st.session_state.interview_questions:

            st.markdown("### 🎯 Your Interview Questions")

            st.markdown(
                st.session_state.interview_questions
            )


    # -----------------------------
    # Learning Resources
    # -----------------------------

    with tab4:

        st.subheader("📚 Personalized Learning Resources")

        st.write(
            "Get learning recommendations based on your missing skills."
        )

        if st.button(
            "📚 Generate Learning Resources",
            key="resources_btn"
        ):

            with st.spinner("Finding relevant learning resources..."):

                try:

                    st.session_state.learning_resources = (
                        generate_learning_resources(
                            role,
                            missing_skills
                        )
                    )

                except Exception as e:

                    st.session_state.learning_resources = (
                        f"⚠️ AI service error:\n\n{str(e)}"
                    )

        if st.session_state.learning_resources:

            st.markdown("### 📖 Recommended Resources")

            st.markdown(
                st.session_state.learning_resources
            )