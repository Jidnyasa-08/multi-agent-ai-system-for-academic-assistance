TECHNICAL REPORT

Project Title

Multi-Agent AI System for Academic Assistance.

Objective

The objective of this project is to develop an AI-powered Academic Assistant Application that assists students with academic information and resources. The system is designed to answer frequently asked questions, provide course-related details, retrieve student information, and support academic learning through an intelligent assistant.

Project Overview

The Academic Assistant Application is a multi-agent AI-based system designed to provide quick and efficient access to academic information. The system utilizes structured datasets and a backend server to process user queries and deliver relevant responses. The application aims to simplify access to academic resources and improve the overall learning experience for students.

System Components

1. Frontend Interface
Provides a user-friendly interface where users can submit academic queries and receive responses.

2. Backend Server
Processes user requests, manages data access, and generates appropriate responses.

3. Multi-Agent AI System
Analyzes user queries and retrieves relevant information from available datasets.

4. Data Sources
Stores academic information in multiple formats for efficient retrieval and management.

Datasets Used

1. FAQ Dataset (faq.json)
Contains frequently asked academic questions and their corresponding answers.

2. Student Dataset (students.csv)
Contains student-related information such as Student ID, Name, Department, Semester, and CGPA.

3. Course Dataset (courses.xlsx)
Contains course information including Course ID, Course Name, Department, Credits, and Faculty details.

4. Syllabus Dataset (syllabus.pdf)
Contains course objectives, outcomes, modules, assessment patterns, and reference materials.

Technologies Used

- Python
- Flask
- GitHub
- Visual Studio Code (VS Code)
- JSON
- CSV
- XLSX

Project Workflow

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

The backend processes user queries and retrieves relevant information from available datasets before sending the response back to the user.

API Design

1. Home Endpoint

Endpoint: /
Method: GET
Purpose: Verify that the backend server is running successfully.

2. Chat Endpoint (Planned)

Endpoint: /api/chat
Method: POST
Purpose: Process academic queries and generate responses.

Work Completed During Internship

Week 1 – Project Planning and Data Collection

- Selected the Academic Assistant project topic.
- Defined project objectives and requirements.
- Collected academic datasets.
- Created FAQ, student, course, and syllabus datasets.

Week 2 – Data Preparation and Repository Setup

- Organized project folder structure.
- Prepared datasets in JSON, CSV, XLSX, and PDF formats.
- Initialized GitHub repository.
- Configured the development environment using Python and Flask.

Week 3 – System Design and Documentation

- Designed the overall system architecture.
- Created the architecture diagram.
- Prepared API documentation.
- Planned backend workflow.
- Designed frontend wireframe.

Week 4 – Project Organization and Final Documentation

- Organized project files and documentation.
- Prepared technical reports and supporting documents.
- Reviewed repository structure.
- Verified datasets and project resources.
- Prepared the project for final submission.

Expected Features

- Academic Question Answering
- FAQ Support
- Course Information Retrieval
- Student Information Lookup
- Syllabus Assistance
- Conversation History Management
- AI-Based Academic Support

Future Development

The following enhancements are planned for future implementation:

- Implemente AI Agents
- FAQ Agent
- Student Information Agent
- Course Information Agent
- Syllabus Information Agent
- Flask Backend API
- Structured Academic Data Processing

Conclusion

The project successfully completed the planning, dataset preparation, repository organization, system design, and documentation phases during the internship period. The developed architecture, datasets, API design, and project structure provide a strong foundation for implementing a complete AI-powered Academic Assistant Application in future development stages.