TECHNICAL REPORT

Project Title

Multi-Agent AI System for Academic Assistance

---

1. Objective

The objective of this project is to develop an AI-powered Academic Assistant Application that helps students access academic information and resources efficiently. The system is designed to answer frequently asked questions, provide course-related details, retrieve student information, and support academic learning through an intelligent assistant.

---

2. Project Overview

The Multi-Agent AI System for Academic Assistance is an AI-based application designed to provide quick and efficient access to academic resources. The system uses structured datasets and a backend server to process user queries and generate relevant responses.

The main goal of this project is to simplify academic information retrieval and improve the learning experience by providing students with an intelligent platform for academic assistance.

---

3. System Components

3.1 Frontend Interface

The frontend interface provides a user-friendly platform where students can enter academic queries and receive responses from the system.

3.2 Backend Server

The backend server handles user requests, manages data processing, accesses academic datasets, and generates appropriate responses.

3.3 Multi-Agent AI System

The multi-agent AI system analyzes user queries and retrieves relevant information from different academic data sources.

3.4 Data Sources

The system stores academic information in multiple structured formats, allowing efficient data retrieval and management.

---

4. Datasets Used

4.1 FAQ Dataset (faq.json)

This dataset contains frequently asked academic questions along with their corresponding answers. It helps the system provide quick responses to common student queries.

4.2 Student Dataset (students.csv)

This dataset contains student-related information such as:

- Student ID
- Student Name
- Department
- Semester
- CGPA

4.3 Course Dataset (courses.xlsx)

This dataset stores course-related information including:

- Course ID
- Course Name
- Department
- Credits
- Faculty Details

4.4 Syllabus Dataset (syllabus.pdf)

This dataset contains academic syllabus information including:

- Course Objectives
- Course Outcomes
- Modules
- Assessment Pattern
- Reference Materials

---

5. Technologies Used

The following technologies and tools were used during the development process:

- Python – Backend programming language
- Flask – Backend web framework for API development
- GitHub – Version control and project repository management
- Visual Studio Code (VS Code) – Development environment
- JSON – Data storage format for FAQ information
- CSV – Student dataset management
- XLSX – Course dataset management
- PDF – Syllabus document storage

---

6. Project Workflow

The system follows a client-server architecture.

Workflow:

User
  ↓
Frontend Interface
  ↓
Backend Server
  ↓
Academic Data Sources
  ↓
Response Generation
  ↓
User

The backend processes user queries, retrieves required information from available datasets, and sends the generated response back to the user.

---

7. API Design

7.1 Home Endpoint

Endpoint: "/"
Method: GET

Purpose:
Used to verify that the backend server is running successfully.

---

7.2 Chat Endpoint

Endpoint: "/api/chat"
Method: POST

Purpose:
Processes academic queries submitted by users and generates appropriate responses.

---

8. Work Completed During Internship

Week 1 – Project Planning and Data Collection

Activities completed:

- Selected the Academic Assistant project topic.
- Defined project objectives and requirements.
- Collected academic datasets.
- Created FAQ, student, course, and syllabus datasets.

---

Week 2 – Data Preparation and Repository Setup

Activities completed:

- Organized project folder structure.
- Prepared datasets in JSON, CSV, XLSX, and PDF formats.
- Created and configured GitHub repository.
- Set up the development environment using Python and Flask.

---

Week 3 – System Design and Documentation

Activities completed:

- Designed the overall system architecture.
- Created architecture documentation.
- Prepared API documentation.
- Planned backend workflow.
- Designed frontend wireframe.

---

Week 4 – Project Organization and Final Documentation

Activities completed:

- Organized project files and documentation.
- Prepared technical reports and supporting documents.
- Reviewed repository structure.
- Verified datasets and project resources.
- Prepared the project for final submission.

---

9. Expected Features

The proposed system includes the following features:

- Academic Question Answering
- FAQ Support
- Course Information Retrieval
- Student Information Lookup
- Syllabus Assistance
- Conversation History Management
- AI-Based Academic Support

---

10. Future Development

Future improvements planned for the system include:

- Implementation of AI Agents
- FAQ Agent Development
- Student Information Agent Development
- Course Information Agent Development
- Syllabus Information Agent Development
- Flask Backend API Enhancement
- Advanced Academic Data Processing

---

11. Conclusion

The project successfully completed the planning, dataset preparation, repository organization, system design, and documentation phases during the internship period.

The developed architecture, datasets, API design, and project structure provide a strong foundation for implementing a complete AI-powered Academic Assistant Application in future development stages.