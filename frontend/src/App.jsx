import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");
  const [message, setMessage] = useState("");
  const [skills, setSkills] = useState({});
  const [jobDescription, setJobDescription] = useState("");
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadResume = async () => {
    if (!file) {
      setMessage("Please select a PDF to upload.");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    try {
      setLoading(true);
      setMessage("Uploading resume...");

      const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        setMessage(data.error);
        return;
      }

      setMessage(data.message);
      setText(data.text);
      setSkills(data.skills);
      setAnalysis(null);
    } catch (error) {
  console.error(error);
  setMessage("Could not connect to backend.");
} finally {
  setLoading(false);
}
  };

  const handleAnalyze = async () => {
    if (Object.keys(skills).length === 0) {
      setMessage("Please upload your resume first.");
      return;
    }

    if (!jobDescription.trim()) {
      setMessage("Please enter a job description.");
      return;
    }

    try {
      setLoading(true);

      const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          resume_skills: skills,
          job_description: jobDescription,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        setMessage(data.error);
        return;
      }

      setAnalysis(data.analysis);
      setMessage("Analysis completed successfully.");
    } catch (error) {
  console.error(error);
  setMessage("Could not connect to backend.");
} finally {
  setLoading(false);
}
  };

  const totalSkills = Object.values(skills).flat().length;

  return (
    <div className="app">
      <header className="header">
        <div className="header-content">
          <h2>Resume<span>Check</span></h2>
          <p>Resume Skill Gap Analyzer</p>
        </div>
      </header>

      <main className="container">
        <section className="intro">
          <h1>Resume Skill Gap Analyzer</h1>
          <p>
            Compare your resume with a job description and identify
            the skills that match and the skills you need to improve.
          </p>
        </section>

        <div className="main-grid">
          <section className="card">
            <h2>Upload Resume</h2>
            <p className="description">
              Upload your resume in PDF format.
            </p>

            <div className="upload-box">
              <input
                type="file"
                accept=".pdf"
                onChange={(e) => setFile(e.target.files[0])}
              />

              {file && (
                <p className="file-name">{file.name}</p>
              )}
            </div>

            <button
              className="primary-button"
              onClick={uploadResume}
              disabled={loading}
            >
              {loading ? "Please wait..." : "Upload Resume"}
            </button>

            {message && <p className="status">{message}</p>}

            {text && (
              <div className="resume-info">
                <h3>Resume Uploaded</h3>
                <p text-align="center">Your resume text has been extracted successfully.</p>

                <details>
                  <summary>View Extracted Text</summary>
                  <pre>{text}</pre>
                </details>
              </div>
            )}
          </section>

          <section className="card">
            <h2>Job Description</h2>
            <p className="description">
              Paste the job description you want to compare against.
            </p>

            <textarea
              placeholder="Paste the job description here..."
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
            />

            <button
              className="primary-button"
              onClick={handleAnalyze}
              disabled={loading}
            >
              {loading ? "Analyzing..." : "Analyze Resume"}
            </button>
          </section>
        </div>

        {Object.keys(skills).length > 0 && (
          <section className="card results-section">
            <div className="section-heading">
              <div>
                <h2>Detected Skills</h2>
                <p className="description">
                  Skills identified from your resume.
                </p>
              </div>

              <span className="count-badge">
                {totalSkills} Skills Found
              </span>
            </div>

            <div className="skills-grid">
              {Object.entries(skills).map(([category, skillList]) => (
                skillList.length > 0 && (
                  <div className="skill-category" key={category}>
                    <h3>{category.replace("_", " ")}</h3>

                    <div className="skill-list">
                      {skillList.map((skill) => (
                        <span className="skill-tag" key={skill}>
                          {skill}
                        </span>
                      ))}
                    </div>
                  </div>
                )
              ))}
            </div>
          </section>
        )}

        {analysis && (
          <section className="card results-section">
            <h2>Analysis Results</h2>
            <p className="description">
              Your resume compared with the job requirements.
            </p>

            <div className="score-container">
              <div className="score">
                <h1>{analysis.score}%</h1>
                <p>Resume Match</p>
              </div>

              <div className="score-bar">
                <div
                  className="score-fill"
                  style={{ width: `${analysis.score}%` }}
                ></div>
              </div>
            </div>

            <div className="analysis-grid">
              <div className="analysis-card matched">
                <h3>Matched Skills</h3>
                <p>{analysis.matched_skills.length} skills</p>
                <div className="skill-list">
                  {analysis.matched_skills.map((skill) => (
                    <span className="skill-tag" key={skill}>
                      {skill}
                    </span>
                  ))}
                </div>
              </div>

              <div className="analysis-card missing">
                <h3>Missing Skills</h3>
                <p>{analysis.missing_skills.length} skills</p>
                <div className="skill-list">
                  {analysis.missing_skills.map((skill) => (
                    <span className="skill-tag" key={skill}>
                      {skill}
                    </span>
                  ))}
                </div>
              </div>

              <div className="analysis-card extra">
                <h3>Additional Skills</h3>
                <p>{analysis.extra_skills.length} skills</p>
                <div className="skill-list">
                  {analysis.extra_skills.map((skill) => (
                    <span className="skill-tag" key={skill}>
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          </section>
        )}

        <footer>
          ResumeCheck | Resume Skill Gap Analyzer
        </footer>
      </main>
    </div>
  );
}

export default App;