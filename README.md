# Resume Skill Gap Analyzer

A web-based application that analyzes resumes against job descriptions to identify matching skills, missing skills, and additional skills. It helps job seekers understand how well their resumes align with specific job requirements and identify areas for improvement.

## Features

- **Resume Upload:** Upload resumes in PDF format.
- **Text Extraction:** Extract text from uploaded PDF resumes.
- **Skill Extraction:** Automatically identify technical skills from resumes using a predefined skill database.
- **Job Description Analysis:** Extract required skills from a given job description.
- **Skill Matching:** Compare resume skills with job requirements.
- **Match Score:** Calculate a percentage-based score representing how closely the resume matches the job description.
- **Skill Gap Identification:** Display matched, missing, and additional skills.
- **Interactive Dashboard:** View analysis results through a simple and user-friendly interface.

## Application Screenshots

### Home Page
<p align="center">
  <img src="screenshots/home.png" width="80%">
</p>

### Resume Upload and Job Description

<p align="center">
  <img src="screenshots/upload.png" width="48%" alt="Resume Upload">
  <img src="screenshots/JD-sample.png" width="48%" alt="Job Description">
</p>

<p align="center">
  <b>Resume Upload</b>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<b>Job Description</b>
</p>

### Skill Gap Analysis
<p align="center">
  <img src="screenshots/analysis.png" width="80%">
</p>
## Technology Stack

### Frontend
- React.js
- Vite
- JavaScript
- CSS

### Backend
- Python
- Flask
- Flask-CORS
- PyMuPDF

### Tools
- Visual Studio Code
- Git
- GitHub

## Project Structure

```text
Resume-Skill-Gap-Analyzer/
│
├── backend/
│   ├── app.py
│   ├── parser.py
│   ├── skill_extractor.py
│   ├── analyzer.py
│   └── skills.json
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

## Installation and Setup

### Requirements

- Python 3.12
- Node.js and npm

### 1. Clone the repository

```powershell
git clone https://github.com/Prathik-N-B/Resume-Skill-Gap-Analyzer.git
cd Resume-Skill-Gap-Analyzer
```

### 2. Install backend dependencies

Run these commands from the project root:

```powershell
py -m venv backend\.venv
.\backend\.venv\Scripts\python.exe -m pip install -r .\backend\requirements-dev.txt
```

### 3. Configure and install the frontend

Create `frontend\.env.local` with:

```env
VITE_API_URL=http://127.0.0.1:5000
```

Then install the frontend dependencies:

```powershell
cd .\frontend
npm install
```

### 4. Run the application

Open two terminals at the project root.

In the first terminal, start the backend:

```powershell
.\backend\.venv\Scripts\python.exe .\backend\app.py
```

In the second terminal, start the frontend:

```powershell
cd .\frontend
npm run dev
```

Open the URL Vite prints in the terminal, usually `http://localhost:5173`.

### 5. Run backend tests

From the project root:

```powershell
.\backend\.venv\Scripts\python.exe -m pytest .\backend\tests
```

## How It Works

1. Upload a resume in PDF format.
2. The backend extracts the text from the uploaded resume using PyMuPDF.
3. The skill extraction module identifies relevant technical skills using a predefined skill database.
4. Enter a job description for the desired role.
5. The application extracts the required skills from the job description.
6. The analyzer compares the extracted resume skills with the job requirements.
7. The application calculates a match percentage and displays:
   - **Matched Skills:** Skills present in both the resume and job description.
   - **Missing Skills:** Skills required by the job description but absent from the resume.
   - **Additional Skills:** Skills found in the resume but not required by the job description.

## Skill Categories

The skill database includes categories such as:

- Programming Languages
- Frontend Development
- Backend Development
- Databases
- Tools and Technologies
- Data Science and Artificial Intelligence
- Computer Science Fundamentals

## Future Enhancements

- Integration with AI-based skill extraction.
- Support for additional resume formats such as DOCX.
- Expanded skill database and job-role-specific skill recommendations.
- Resume improvement suggestions.
- Resume parsing and analysis using NLP techniques.
- Deployment for public access.

## Author

**Prathik N B**

Information Science and Engineering

[GitHub Profile](https://github.com/Prathik-N-B)

---

If you find this project useful, consider giving the repository a ⭐.