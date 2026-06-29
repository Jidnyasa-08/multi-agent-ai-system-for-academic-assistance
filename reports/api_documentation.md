API Documentation

Project

Multi-Agent AI System for Academic Assistant Application

API Endpoints

Endpoint| Method| Purpose
/api/chat| POST| Send academic questions to the AI system
/api/quiz| POST| Generate quiz questions
/api/summary| POST| Generate topic summaries
/api/history| GET| Retrieve previous interactions
/api/feedback| POST| Submit user feedback
/api/health| GET| Check server status

Example Request

POST /api/chat

Request:
{
"question": "What is Artificial Intelligence?"
}

Response:
{
"answer": "Artificial Intelligence is the simulation of human intelligence by machines."
}

Example Health Check

GET /api/health

Response:
{
"status": "Server Running"
}