from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import pandas as pd

from agents.faq_agent import get_faq_answer
from agents.course_agent import get_course_answer
from agents.student_agent import get_student_answer
from agents.syllabus_agent import get_syllabus_answer

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "..", "data", "cleaned")

# Load FAQ JSON
with open(
    os.path.join(DATA_DIR, "faq_cleaned.json"),
    "r",
    encoding="utf-8"
) as file:
    faq_data = json.load(file)

# Load Course Excel
course_data = pd.read_excel(
    os.path.join(DATA_DIR, "courses_cleaned.xlsx")
)

# Load Student CSV
student_data = pd.read_csv(
    os.path.join(DATA_DIR, "students_cleaned.csv")
)

# Syllabus Content
pdf_text = """
Introduction to Artificial Intelligence
Course Code: C105
Department: Computer Science Engineering (CSE)

Course Objectives
Understand the fundamentals of Artificial Intelligence.
Learn about intelligent agents and problem-solving techniques.
Understand basic Machine Learning concepts.
Develop analytical and critical thinking skills.
Apply AI concepts to solve academic and real-world problems.

Course Outcomes
Explain the basic concepts of Artificial Intelligence.
Design simple AI-based solutions.
Apply search algorithms to solve problems.
Understand the basics of Machine Learning.
Use AI concepts in academic assistance systems.

Course Modules

Unit 1: Introduction to Artificial Intelligence
Definition and History of AI
Applications of AI
Intelligent Agents

Unit 2: Problem Solving
State Space Search
Breadth First Search
Depth First Search
Heuristic Search

Unit 3: Machine Learning Basics
Supervised Learning
Unsupervised Learning
Classification
Regression

Unit 4: Knowledge Representation
Logic
Semantic Networks
Frames
Rule-Based Systems

Unit 5: AI Applications
Chatbots
Recommendation Systems
Academic Assistance
Healthcare
Education

Assessment Pattern
Internal Assessment: 30 Marks
End Semester Examination: 70 Marks

Reference Books
Artificial Intelligence – Stuart Russell & Peter Norvig
Artificial Intelligence: A Modern Approach
Introduction to Machine Learning
"""

@app.route("/")
def home():
    return "Academic Assistant Multi-Agent Backend Running"


@app.route("/api/chat", methods=["POST"])
def chat():

    user_question = request.json.get("question", "")

    # FAQ Agent
    answer = get_faq_answer(user_question, faq_data)
    if answer:
        return jsonify({
            "agent": "FAQ Agent",
            "answer": answer
        })

    # Course Agent
    answer = get_course_answer(user_question, course_data)
    if answer:
        return jsonify({
            "agent": "Course Agent",
            "answer": answer
        })

    # Student Agent
    answer = get_student_answer(user_question, student_data)
    if answer:
        return jsonify({
            "agent": "Student Agent",
            "answer": answer
        })

    # Syllabus Agent
    answer = get_syllabus_answer(user_question, pdf_text)
    if answer:
        return jsonify({
            "agent": "Syllabus Agent",
            "answer": answer
        })

    return jsonify({
        "agent": "Router",
        "answer": "Sorry, I could not find an answer."
    })


if __name__ == "__main__":
    app.run(debug=True)