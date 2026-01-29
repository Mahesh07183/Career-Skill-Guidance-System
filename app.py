from flask import Flask, jsonify, render_template, request
import pandas as pd
import os


# ---------------------------------
# Flask app initialization
# ---------------------------------
app = Flask(__name__)

# ---------------------------------
# Load dataset
# ---------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "studies_career.csv")

df = pd.read_csv(DATA_PATH)

# ---------------------------------
# Subject → Skill mapping
# ---------------------------------
subject_skill_map = {
    "math_score": ["problem solving", "statistics"],
    "physics_score": ["analytical thinking"],
    "chemistry_score": ["data analysis"],
    "biology_score": ["research skills"],
    "english_score": ["communication"],
    "geography_score": ["data interpretation"],
    "history_score": ["critical thinking"]
}

# ---------------------------------
# Career → Required skills mapping
# ---------------------------------
career_skill_map = {
    "data scientist": [
        "statistics",
        "data analysis",
        "problem solving",
        "analytical thinking",
        "communication"
    ],
    "software engineer": [
        "problem solving",
        "analytical thinking",
        "critical thinking"
    ],
    "analyst": [
        "data analysis",
        "data interpretation",
        "communication"
    ],
    "researcher": [
        "research skills",
        "analytical thinking",
        "communication"
    ],
    "doctor": [
        "research skills",
        "analytical thinking",
        "communication",
        "data analysis"
    ],
    "lawyer": [
        "critical thinking",
        "communication",
        "data interpretation"
    ],
    "teacher": [
        "communication",
        "critical thinking",
        "research skills"
    ],
    "scientist": [
        "research skills",
        "analytical thinking",
        "data analysis",
        "problem solving"
    ],
    "business owner": [
        "problem solving",
        "communication",
        "data interpretation",
        "analytical thinking"
    ],
    "government officer": [
        "data interpretation",
        "communication",
        "critical thinking",
        "analytical thinking"
    ],
    "artist": [
        "critical thinking",
        "communication"
    ]
}

# ---------------------------------
# Helper functions
# ---------------------------------
def get_strong_subjects(row, threshold=75):
    return [sub for sub in subject_skill_map if row[sub] >= threshold]

def derive_skills_from_subjects(subjects):
    skills = set()
    for sub in subjects:
        skills.update(subject_skill_map[sub])
    return list(skills)

# ---------------------------------
# ROUTES
# ---------------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "Career Skill Guidance System is running",
        "port": 5000
    })

@app.route("/ui")
def ui():
    return render_template("index.html")

@app.route("/recommend")
def recommend():
    # simulate a completed student (first record)
    user = df.iloc[0]

    career = user["career_aspiration"].lower()
    strong_subjects = get_strong_subjects(user)
    current_skills = derive_skills_from_subjects(strong_subjects)

    required_skills = career_skill_map.get(career, [])
    skills_to_learn = list(set(required_skills) - set(current_skills))

    return jsonify({
        "career_aspiration": career,
        "strong_subjects": strong_subjects,
        "current_skills": current_skills,
        "skills_to_learn_next": skills_to_learn
    })

@app.route("/recommend_ui")
def recommend_ui():
    career = request.args.get("career", "").lower()
    
    if not career:
        return render_template("index.html", error="Please enter a career aspiration")

    user = df.iloc[0]  # simulate a completed student
    strong_subjects = get_strong_subjects(user)
    current_skills = derive_skills_from_subjects(strong_subjects)

    required_skills = career_skill_map.get(career, [])
    
    if not required_skills:
        return render_template(
            "index.html",
            career=career,
            error=f"Career '{career}' not found in the system. Try: data scientist, software engineer, analyst, researcher, doctor, lawyer, teacher, scientist, business owner, government officer, artist"
        )
    
    skills_to_learn = list(set(required_skills) - set(current_skills))

    return render_template(
        "index.html",
        career=career,
        skills=skills_to_learn,
        current_skills=current_skills,
        required_skills=required_skills
    )

# ---------------------------------
# Run server
# ---------------------------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
