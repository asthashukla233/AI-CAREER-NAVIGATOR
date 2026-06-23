import json

def analyze_gap(
    user_skills,
    user_subjects,
    user_projects,
    role,
    package
):
    with open("data/roles.json", "r") as f:
        roles = json.load(f)

    target = roles[role]["packages"][package]

    required_skills = target["skills"]
    required_subjects = target["core_subjects"]

    missing_skills = list(
        set(required_skills) - set(user_skills)
    )

    missing_subjects = list(
        set(required_subjects) - set(user_subjects)
    )

    project_gap = max(
        0,
        target["projects"] - user_projects
    )

    return {
        "required_skills": required_skills,
        "missing_skills": missing_skills,
        "required_subjects": required_subjects,
        "missing_subjects": missing_subjects,
        "required_projects": target["projects"],
        "project_gap": project_gap,
        "required_dsa": target["dsa_level"]
    }