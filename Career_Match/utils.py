from skills_list import SKILLS

# Extract skills from text
def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS if skill in text]

# Compare skills between JD and resume
def skill_gap(job_skills, resume_skills):
    matched = list(set(job_skills) & set(resume_skills))
    missing = list(set(job_skills) - set(resume_skills))
    return matched, missing

# Generate actionable tip
def generate_tip(matched, missing):
    if missing:
        return f"The role requires '{missing[0]}'. Consider learning it or adding a project."
    elif matched:
        return f"Highlight your experience in '{matched[0]}' in projects or internships."
    else:
        return "Add more technical details and projects to your resume."
