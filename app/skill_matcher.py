#Finds matched/missing keywords between a resume and a job description and gives a match score.
def match_skills(resume_text, job_text):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_text.lower().split())
    matched = resume_words & job_words
    missing = job_words - resume_words
    score = len(matched) / len(job_words) * 100
    return round(score), matched, missing