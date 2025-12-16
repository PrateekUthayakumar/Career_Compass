import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from skills_list import SKILLS

# Load models
nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer("all-MiniLM-L6-v2")


# -------- Skill Extraction using spaCy --------
def extract_skills(text):
    text = text.lower()
    doc = nlp(text)

    found_skills = set()

    for token in doc:
        if token.text in SKILLS:
            found_skills.add(token.text)

    for skill in SKILLS:
        if skill in text:
            found_skills.add(skill)

    return list(found_skills)


# -------- Main Analyzer --------
def analyze_job_resume(job_desc, resume_text):

    # 1️⃣ Semantic Similarity (AI)
    jd_vec = model.encode(job_desc)
    resume_vec = model.encode(resume_text)

    similarity = cosine_similarity(
        [jd_vec], [resume_vec]
    )[0][0]

    score = round(similarity * 10, 1)

    # 2️⃣ Skill Extraction
    job_skills = extract_skills(job_desc)
    resume_skills = extract_skills(resume_text)

    matched = list(set(job_skills) & set(resume_skills))
    missing = list(set(job_skills) - set(resume_skills))

    # 3️⃣ Rule-based Intelligent Tip
    if missing:
        tip = f"Consider learning or highlighting experience in {missing[0]}."
    elif matched:
        tip = f"Strong alignment. Emphasize your experience with {matched[0]}."
    else:
        tip = "Add relevant technical skills and projects related to this role."

    return score, matched, missing, tip
