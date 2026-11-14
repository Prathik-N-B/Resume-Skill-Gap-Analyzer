import json
import re
from pathlib import Path

SKILL_ALIASES = {
    "node.js": ("node.js", "nodejs"),
    "scikit-learn": ("scikit-learn", "scikit learn"),
    "c#": ("c#", "c sharp"),
}


def load_skills():
    skills_path = Path(__file__).resolve().with_name("skills.json")
    with skills_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def extract_skills(text):
    skills_data = load_skills()
    text = text.casefold()
    detected_skills = {}

    for category, skills in skills_data.items():
        detected_skills[category] = []

        for skill in skills:
            aliases = SKILL_ALIASES.get(skill.casefold(), (skill,))

            for alias in aliases:
                pattern = rf"(?<!\w){re.escape(alias.casefold())}(?!\w)"

                if skill.casefold() == "c":
                    pattern = r"(?<!\w)c(?![\w+#])"

                if re.search(pattern, text):
                    detected_skills[category].append(skill)
                    break

    return detected_skills