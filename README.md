# Notes API

A simple RESTful Notes API built using FastAPI, SQLAlchemy, SQLite, and Pydantic.  
This project demonstrates backend development fundamentals including CRUD operations, database relationships, request validation, and API documentation.

---

## Features

- User management system
- Create and retrieve notes
- One-to-many relationship between users and notes
- SQLite database integration
- SQLAlchemy ORM models
- Pydantic validation schemas
- Automatic Swagger API documentation
- Clean modular project structure

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

## API Endpoints

### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users` | Get all users |
| GET | `/users/{user_id}` | Get a specific user |
| POST | `/users` | Create a new user |

### Notes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/notes` | Get all notes |
| POST | `/notes` | Create a new note |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
```

Move into the project folder:

```bash
cd your-repo-name
```

Install dependencies:

```bash
pip install fastapi sqlalchemy uvicorn pydantic
```

---

## Run the Server

```bash
uvicorn main:app --reload
```

Server will run on:

```text
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Project Structure

```text
project/
│
├── main.py
├── models.py
├── schema.py
├── database.py
├── notes.db
└── requirements.txt
```

---

## Example Request

### Create User

```json
{
  "name": "Nour Yehia",
  "age": 22
}
```

### Create Note

```json
{
  "user_id": 1,
  "category": "study",
  "content": "Learn FastAPI"
}
```

---

## Topics

`fastapi` `python` `sqlalchemy` `sqlite` `pydantic` `rest-api` `crud` `backend`

---

## License

This project is open-source and available for learning and educational purposes.
