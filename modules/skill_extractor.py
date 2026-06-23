def extract_skills(text):

    skills_db = [
        "python",
        "java",
        "c++",
        "sql",
        "mysql",
        "mongodb",
        "aws",
        "docker",
        "kubernetes",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "langchain",
        "react",
        "javascript",
        "html",
        "css",
        "git",
        "github",
        "power bi"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))