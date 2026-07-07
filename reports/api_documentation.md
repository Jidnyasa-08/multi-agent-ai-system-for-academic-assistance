# API Documentation

## Project
**Multi-Agent AI System for Academic Assistant**

---

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| / | GET | Check backend server status |
| /api/chat | POST | Send academic questions to the AI system |

---

## Example Request

**POST /api/chat**

Request:

```json
{
  "question": "What is the minimum attendance required?"
}
```

Response:

```json
{
  "agent": "FAQ Agent",
  "answer": "Students must maintain at least 75% attendance."
}
```

---

## Example Health Check

**GET /**

Response:

```text
Academic Assistant Multi-Agent Backend Running
```