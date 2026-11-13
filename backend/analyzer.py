def analyze_skills(resume_skills, job_skills):
    resume_set = set()

    for skills in resume_skills.values():
        resume_set.update(skills)

    job_set = set()

    for skills in job_skills.values():
        job_set.update(skills)

    matched_skills = sorted(resume_set.intersection(job_set))
    missing_skills = sorted(job_set.difference(resume_set))
    extra_skills = sorted(resume_set.difference(job_set))

    if len(job_set) > 0:
        match_score = round((len(matched_skills)/len(job_set))*100)
    else:
        match_score = 0
    return {
        "score": match_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "extra_skills": extra_skills
    }                