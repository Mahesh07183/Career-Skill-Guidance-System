import os
import pandas as pd

# Resolve project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "studies_career.csv")

# Load dataset
df = pd.read_csv(DATA_PATH)

print("Dataset Loaded Successfully")
print(df.head())
print("Columns in dataset:")
print(df.columns)
# =============================
# USER PROFILE (COMPLETED STUDENT)
# =============================
# Current skills of the user (after completing studies)
user_current_skills = ["python", "sql", "ml"]

# Target career role the user wants
target_career = "data scientist"
# =============================
# STEP 1: Subject → Skill Mapping
# =============================
subject_skill_map = {
    "math_score": ["problem solving", "statistics"],
    "physics_score": ["analytical thinking"],
    "chemistry_score": ["data analysis"],
    "biology_score": ["research skills"],
    "english_score": ["communication"],
    "geography_score": ["data interpretation"],
    "history_score": ["critical thinking"]
}
# =============================
# STEP 2: Career → Required Skills
# =============================
career_skill_map = {
    "data scientist": [
        "statistics", "data analysis", "problem solving",
        "analytical thinking", "communication"
    ],
    "software engineer": [
        "problem solving", "analytical thinking",
        "critical thinking"
    ],
    "researcher": [
        "research skills", "analytical thinking",
        "communication"
    ],
    "analyst": [
        "data analysis", "data interpretation",
        "communication"
    ]
}
# =============================
# STEP 3: Identify Strong Subjects
# =============================
def get_strong_subjects(row, threshold=75):
    strong_subjects = []
    for subject in subject_skill_map:
        if row[subject] >= threshold:
            strong_subjects.append(subject)
    return strong_subjects
# =============================
# STEP 4: Derive Current Skills
# =============================
def derive_skills_from_subjects(subjects):
    skills = set()
    for sub in subjects:
        skills.update(subject_skill_map[sub])
    return list(skills)
# =============================
# STEP 5: Select User Profile
# =============================
user = df.iloc[0]  # simulate one graduate

user_career = user["career_aspiration"].lower()
strong_subjects = get_strong_subjects(user)
user_current_skills = derive_skills_from_subjects(strong_subjects)

print("\n👤 USER PROFILE")
print("Career Aspiration:", user_career)
print("Strong Subjects:", strong_subjects)
print("Derived Skills:", user_current_skills)
# =============================
# STEP 6: Skill Gap Analysis
# =============================
required_skills = career_skill_map.get(user_career, [])

missing_skills = set(required_skills) - set(user_current_skills)
print("\n🎯 CAREER GUIDANCE RESULT")

print("Current Skills:", user_current_skills)
print("Required Skills for Career:", required_skills)

print("\n📌 Skills to Learn Next:")
if missing_skills:
    for skill in missing_skills:
        print("-", skill)
else:
    print("You already have the required foundational skills!")
