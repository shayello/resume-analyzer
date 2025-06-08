from fastapi import FastAPI, UploadFile, Form
from app.resume_parser import extract_text_from_pdf
from app.skill_matcher import match_skills
from app.ai_suggestions import get_resume_improvement_suggestion
#Accepts uploads, runs the analyzer, and returns JSON results.
app = FastAPI()

@app.post("/analyze/")
async def analyze(resume: UploadFile, job_desc: str = Form(...)):
    contents = await resume.read()
    with open("temp_resume.pdf", "wb") as f:
        f.write(contents)

    resume_text = extract_text_from_pdf("temp_resume.pdf")
    score, matched, missing = match_skills(resume_text, job_desc)
    suggestion = get_resume_improvement_suggestion(resume_text, job_desc)

    return {
        "match_score": score,
        "matched_skills": list(matched),
        "missing_skills": list(missing),
        "ai_suggestion": suggestion
    }