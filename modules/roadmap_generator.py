def generate_roadmap(missing_skills):

    roadmap = []

    for i, skill in enumerate(missing_skills, start=1):

        roadmap.append({
            "week": i,
            "focus": skill,
            "tasks": [
                f"Learn fundamentals of {skill}",
                f"Build mini project using {skill}",
                f"Practice interview questions on {skill}"
            ]
        })

    return roadmap