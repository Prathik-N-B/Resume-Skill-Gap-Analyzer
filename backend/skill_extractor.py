import json
import re

def load_skills():
    with open("skills.json","r",encoding="utf-8") as file:
        return json.load(file)

def extract_skills(text):
    skills_data = load_skills()

    text = text.lower()

    detected_skills = {}

    for category, skills in skills_data.items():
        detected_skills[category] = []

        for skill in skills:
            pattern = r"\b" + re.escape(skill.lower()) + r"\b"
            if re.search(pattern, text):
                detected_skills[category].append(skill)

    return detected_skills