import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
#Asks ChatGPT how to improve the resume to match the job
def get_resume_improvement_suggestion(resume, job_desc):
    prompt = f"Here is a resume:\n{resume}\n\nAnd a job description:\n{job_desc}\n\nHow can this resume be improved to better match the job?"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperatue=0.7,
        max_tokens=150
    )
    return response['choices'][0]['messages']['content'].strip()
