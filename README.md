# 🧠 Resume Analyzer + Job Match Recommender

An AI-powered web app that analyzes resumes and recommends personalized job matches using FastAPI, OpenAI, and modern Python tooling.

## 🚀 Features

- 📄 Upload or paste resume text
- 🧠 Extract skills and experience using LLMs (OpenAI)
- 💼 Recommend matching jobs based on your profile
- ⚙️ Built with FastAPI for blazing-fast APIs
- 📊 Scalable for future integration with job APIs and dashboards

## 🛠 Tech Stack

- **Backend**: Python, FastAPI
- **AI/LLM**: OpenAI GPT-4 (or GPT-3.5)
- **Parsing/Extraction**: Langchain (optional), regex, SpaCy
- **Deployment**: Localhost with Uvicorn

## 🧑‍💻 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/resume-analyzer.git
cd resume-analyzer
```

### 2. Create Virtual Env & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Run the App
```bash
uvicorn app.main:app --reload
```

- Then open your browser to:  http://127.0.0.1:8000/docs

## Project Structure
```resume-analyzer/

├── app/
│   ├── main.py                  ← FastAPI app
│   ├── parser.py                ← extract_text_from_pdf() lives here
│   ├── skill_matcher.py         ← match_skills() lives here
│   └── ai_suggestions.py        ← get_resume_improvement_suggestion() lives here
├── requirements.txt
├── README.md
└── .gitignore
```

🤝 Contributing
Pull requests welcome! For major changes, please open an issue first to discuss what you’d like to change.
