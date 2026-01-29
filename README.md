# Career Skill Guidance System

A Flask-based web application that helps students and professionals identify the skills they need to develop based on their academic strengths and career aspirations.

## 📋 Project Overview

This system analyzes student academic performance across various subjects and maps those strengths to professional skills. It then provides personalized recommendations on which skills they should focus on developing to pursue their desired career path.

### How It Works

1. **Subject Analysis**: Identifies strong subjects based on a configurable threshold (default: 75/100)
2. **Skill Mapping**: Maps academic subjects to professional competencies
3. **Career Requirements**: Matches career paths to required skill sets
4. **Gap Analysis**: Calculates which skills the student needs to develop

## 🏗️ Project Structure

```
career_course_recommendation/
├── app.py                          # Main Flask application
├── data/
│   └── studies_career.csv          # Student data with scores and career aspirations
├── src/
│   ├── recommender.py              # Recommendation logic (standalone script)
│   └── __pycache__/
├── static/
│   └── style.css                   # Modern styling with gradients and responsive design
├── templates/
│   └── index.html                  # Web UI for the recommendation system
└── README.md                        # This file
```

## 🔧 Key Components

### app.py
The main Flask application with the following features:

- **Route `/`**: Returns API status
- **Route `/ui`**: Serves the web interface
- **Route `/recommend`**: JSON API that recommends skills based on the first student record
- **Route `/recommend_ui`**: Web form handler for career recommendations

### Data Flow

1. Loads student data from CSV with columns:
   - Student demographics (name, email, gender)
   - Academic scores (math, physics, chemistry, biology, english, geography, history)
   - Career aspiration

2. Applies subject-to-skill mapping:
   ```
   Math Score → Problem Solving, Statistics
   Physics → Analytical Thinking
   Chemistry → Data Analysis
   Biology → Research Skills
   English → Communication
   Geography → Data Interpretation
   History → Critical Thinking
   ```

3. Maps careers to required skills:
   - **Data Scientist**: Statistics, Data Analysis, Problem Solving, Analytical Thinking, Communication
   - **Software Engineer**: Problem Solving, Analytical Thinking, Critical Thinking
   - **Analyst**: Data Analysis, Data Interpretation, Communication
   - **Researcher**: Research Skills, Analytical Thinking, Communication
   - **Doctor**: Research Skills, Analytical Thinking, Communication, Data Analysis
   - **Lawyer**: Critical Thinking, Communication, Data Interpretation
   - **Teacher**: Communication, Critical Thinking, Research Skills
   - **Scientist**: Research Skills, Analytical Thinking, Data Analysis, Problem Solving
   - **Business Owner**: Problem Solving, Communication, Data Interpretation, Analytical Thinking
   - **Government Officer**: Data Interpretation, Communication, Critical Thinking, Analytical Thinking
   - **Artist**: Critical Thinking, Communication

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Flask
- Pandas

### Installation

1. Install dependencies:
```bash
pip install flask pandas
```

2. Run the Flask application:
```bash
python app.py
```

3. Access the application:
   - Web UI: `http://localhost:5000/ui`
   - API: `http://localhost:5000/recommend`

## 📱 Usage

### Web Interface
1. Navigate to `http://localhost:5000/ui`
2. Enter a career aspiration (e.g., "data scientist")
3. Click "Get Skill Guidance"
4. View your:
   - Current skills (derived from strong subjects)
   - Required skills for the career
   - Skills you need to learn next

### API Usage

Get recommendations in JSON format:
```bash
curl http://localhost:5000/recommend
```

Response:
```json
{
    "career_aspiration": "lawyer",
    "strong_subjects": ["math_score", "physics_score", "chemistry_score", ...],
    "current_skills": ["problem solving", "analytical thinking", "communication"],
    "skills_to_learn_next": ["data interpretation", "critical thinking"]
}
```

## 🎨 UI Features

- **Modern Design**: Gradient background with card-based layout
- **Responsive**: Mobile-friendly interface
- **Visual Feedback**: Color-coded skill badges (success, info, primary)
- **Error Handling**: Clear error messages for invalid inputs
- **Comprehensive Display**: Shows current skills, required skills, and skill gaps

## 📊 Data Requirements

The CSV file should include:
- Student identification fields
- Academic scores for all mapped subjects
- Career aspiration field

## 🔄 How the Algorithm Works

### Step 1: Identify Strong Subjects
Compares each subject score against a threshold (default: 75)

### Step 2: Derive Current Skills
For each strong subject, extracts associated skills from the subject-skill mapping

### Step 3: Get Required Skills
Looks up the career path and retrieves required skills

### Step 4: Calculate Skill Gap
Uses set difference: `Required Skills - Current Skills = Skills to Learn`

## 🐛 Issues Fixed

1. **Route Registration Error**: Routes were defined after the Flask app initialization but placed after `if __name__ == "__main__"`, preventing registration
   - ✅ Fixed: Moved all routes before the main block

2. **Limited Career Coverage**: Only 4 careers were mapped
   - ✅ Fixed: Added 7 additional career paths for broader coverage

3. **Poor UI/UX**: Basic styling without proper feedback
   - ✅ Fixed: Enhanced with modern gradient design, error handling, and skill visualization

4. **Missing Input Validation**: No error handling for invalid career inputs
   - ✅ Fixed: Added validation and helpful error messages

## 💡 Future Enhancements

- [ ] User authentication and profile persistence
- [ ] Dynamic career and skill database
- [ ] Personalized learning path recommendations
- [ ] Integration with course catalogues
- [ ] Progress tracking and skill level assessment
- [ ] Skill-based job market insights
- [ ] Multi-student comparison and benchmarking
- [ ] Export recommendations as PDF

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

Career Skill Guidance System Team

---

**Note**: This is a development server. For production deployment, use a WSGI server like Gunicorn or uWSGI.
