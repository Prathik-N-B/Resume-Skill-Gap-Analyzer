CATEGORY_WEIGHTS = {
    "programming": 2.0,
    "frontend": 1.0,
    "backend": 2.0,
    "database": 1.5,
    "tools": 1.0,
    "data_ai": 2.0,
    "other": 1.0,
}


def analyze_skills(resume_skills, job_skills):
    resume_set = {
        skill.casefold()
        for skills in resume_skills.values()
        for skill in skills
    }
    job_set = {
        skill.casefold()
        for skills in job_skills.values()
        for skill in skills
    }

    matched_skills = sorted(resume_set & job_set)
    missing_skills = sorted(job_set - resume_set)
    extra_skills = sorted(resume_set - job_set)

    total_weight = 0.0
    matched_weight = 0.0

    for category, skills in job_skills.items():
        weight = CATEGORY_WEIGHTS.get(category, 1.0)
        unique_skills = {skill.casefold() for skill in skills}

        total_weight += weight * len(unique_skills)
        matched_weight += weight * sum(
            skill in resume_set for skill in unique_skills
        )

    score = round(matched_weight / total_weight * 100) if total_weight else 0

    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "extra_skills": extra_skills,
    }