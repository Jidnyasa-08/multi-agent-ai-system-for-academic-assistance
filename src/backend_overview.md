BACKEND OVERVIEW

Purpose

The backend server handles communication between the frontend interface and the Multi-Agent AI System.

Technology

- Python
- Flask Framework
- Pandas
- JSON

Responsibilities

- Receive user requests
- Process API calls
- Route queries to appropriate AI agents
- Retrieve information from datasets
- Return responses to users

Implemented Components

- FAQ Agent
- Course Agent
- Student Agent
- Syllabus Agent

Datasets Connected

- faq_cleaned.json
- students_cleaned.csv
- courses_cleaned.xlsx
- syllabus_cleaned.pdf

Implemented Endpoint

- /api/chat (POST)

Working Flow

Frontend
↓
Flask Backend
↓
Router Logic
↓
FAQ Agent / Course Agent / Student Agent / Syllabus Agent
↓
Response Returned to User

Future Endpoints

- /api/quiz
- /api/summary
- /api/history
- /api/feedback

Conclusion

The backend successfully processes academic queries through multiple AI agents and retrieves information from structured datasets including JSON, CSV, XLSX, and PDF resources.