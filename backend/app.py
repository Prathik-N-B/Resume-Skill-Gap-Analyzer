from flask import Flask, request, jsonify
from flask_cors import CORS
from parser import extract_text_from_pdf
from skill_extractor import extract_skills
from analyzer import analyze_skills

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
CORS(app)

@app.errorhandler(413)
def request_entity_too_large(_error):
    return jsonify({"error": "The PDF must be 5 MB or smaller."}), 413

@app.route("/")
def home():
    return "Resume Skill Gap Analyzer Backend is running!"

@app.route("/upload", methods=["POST"])
def upload_resume():
    if "resume" not in request.files:
        return jsonify({"error": "No resume uploaded"}), 400

    file = request.files["resume"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    if not file.filename.lower().endswith(".pdf"):
        return jsonify({"error": "Invalid file type. Only PDF files are allowed."}), 400
    
    try:
        text = extract_text_from_pdf(file)
        skills = extract_skills(text)
        return jsonify({
            "message": "Resume uploaded successfully",
            "text": text,
            "skills": skills
        })
    
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

@app.route("/analyze", methods=["POST"])
def analyze_resume():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No data received"}), 400

    resume_skills = data.get("resume_skills", {})
    job_description = data.get("job_description", "")

    if not job_description.strip():
        return jsonify({"error": "Job description is required"}), 400

    job_skills = extract_skills(job_description)

    result = analyze_skills(
        resume_skills,
        job_skills
    )

    return jsonify({
        "job_skills": job_skills,
        "analysis": result
    })
    
if __name__ == "__main__":
    app.run(debug=False, port=5000)