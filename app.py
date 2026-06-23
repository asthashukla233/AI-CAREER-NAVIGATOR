import streamlit as st

from modules.resume_parser import extract_resume_text
from modules.skill_extractor import extract_skills
from modules.gap_analysis import analyze_gap
from modules.roadmap_generator import generate_roadmap

st.set_page_config(
    page_title="Career Navigator AI",
    layout="wide"
)

st.title("🚀 Career Navigator AI")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

role = st.selectbox(
    "Target Role",
    [
        "Data Scientist",
        "AI Engineer",
        "Software Engineer"
    ]
)

package = st.selectbox(
    "Target Package",
    [
        "0-4",
        "5-9",
        "10-14",
        "15-19",
        "20+"
    ]
)

subjects = st.multiselect(
    "Core Subjects Known",
    [
        "oops",
        "dbms",
        "operating systems",
        "computer networks",
        "statistics",
        "probability",
        "linear algebra",
        "machine learning",
        "nlp",
        "deep learning"
    ]
)

project_count = st.slider(
    "Number of Projects",
    0,
    10,
    1
)

if uploaded_file:

    # Resume Parsing
    text = extract_resume_text(uploaded_file)

    # Skill Extraction
    user_skills = extract_skills(text)

    st.subheader("Detected Skills")
    st.write(user_skills)

    # Gap Analysis
    result = analyze_gap(
        user_skills=user_skills,
        user_subjects=subjects,
        user_projects=project_count,
        role=role,
        package=package
    )

    # Missing Skills
    st.subheader("Missing Skills")
    st.write(result["missing_skills"])

    # Missing Subjects
    st.subheader("Missing Core Subjects")
    st.write(result["missing_subjects"])

    # Project Gap
    st.subheader("Project Gap")
    st.write(
        f"Need {result['project_gap']} more project(s)"
    )

    # DSA Requirement
    st.subheader("Required DSA Level")
    st.write(result["required_dsa"])

    # Score Calculations
    skills_score = (
        (len(result["required_skills"]) -
         len(result["missing_skills"]))
        / len(result["required_skills"])
    ) * 100

    subjects_score = (
        (len(result["required_subjects"]) -
         len(result["missing_subjects"]))
        / len(result["required_subjects"])
    ) * 100

    project_score = (
        project_count /
        result["required_projects"]
    ) * 100

    project_score = min(project_score, 100)

    overall_score = (
        skills_score * 0.5 +
        subjects_score * 0.3 +
        project_score * 0.2
    )

    # Readiness Score
    st.subheader("🎯 Career Readiness Score")

    st.progress(overall_score / 100)

    st.metric(
        "Overall Match",
        f"{overall_score:.1f}%"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Skills Match",
            f"{skills_score:.1f}%"
        )

    with col2:
        st.metric(
            "Subjects Match",
            f"{subjects_score:.1f}%"
        )

    with col3:
        st.metric(
            "Projects Match",
            f"{project_score:.1f}%"
        )

    # Roadmap Generation
    roadmap_input = (
        result["missing_skills"]
        + result["missing_subjects"]
    )

    roadmap = generate_roadmap(
        roadmap_input
    )

    st.subheader("🗺️ Personalized Roadmap")

    for step in roadmap:

        st.markdown(
            f"""
### Week {step['week']}
**Focus:** {step['focus']}

- {step['tasks'][0]}
- {step['tasks'][1]}
- {step['tasks'][2]}
"""
        )