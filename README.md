# FastAPI Structure

A production-ready, scalable FastAPI project structure designed to help developers build clean, maintainable, and enterprise-grade REST APIs.

This boilerplate follows a layered architecture that separates routing, business logic, database access, configuration, and utilities, making it easy to scale from small projects to large applications.

---

## ✨ Features

- 🚀 FastAPI
- 📁 Clean and scalable folder structure
- ⚙️ Environment-based configuration
- 🔐 Authentication ready
- 🗄️ SQLAlchemy integration
- 🔄 Alembic migration support
- 📦 Modular routers
- ✅ Pydantic validation
- 🧪 Testing ready
- 📝 Structured logging
- 🐳 Docker support
- 📚 Automatic Swagger & ReDoc documentation

---

# Project Structure

```text
.
├── app/
│   ├── api/
│   │   ├── v1/
│   │   ├── dependencies/
│   │   └── routes/
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── logging.py
│   │
│   ├── database/
│   │   ├── session.py
│   │   ├── base.py
│   │   └── migrations/
│   │
│   ├── models/
│   │
│   ├── schemas/
│   │
│   ├── services/
│   │
│   ├── repositories/
│   │
│   ├── utils/
│   │
│   ├── middleware/
│   │
│   ├── exceptions/
│   │
│   └── main.py
│
├── tests/
├── .env.example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/NikhilRPandey1/fastapi_structure.git

cd fastapi_structure
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Copy

```bash
cp .env.example .env
```

Update the values inside `.env`.

Example

```env
APP_NAME=FastAPI Structure
DEBUG=True

DATABASE_URL=postgresql://user:password@localhost:5432/database

SECRET_KEY=your-secret-key

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Running the Application

Development

```bash
uvicorn app.main:app --reload
```

Production

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

# API Documentation

Once the server is running:

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Architecture

The project follows a layered architecture.

```
Client
    │
    ▼
Router
    │
    ▼
Service
    │
    ▼
Repository
    │
    ▼
Database
```

Each layer has a single responsibility.

- **Router** → Handles HTTP requests
- **Service** → Business logic
- **Repository** → Database operations
- **Schema** → Request/Response validation
- **Model** → Database models

---

# Adding a New Module

Create:

```
models/
schemas/
services/
repositories/
routers/
```

Register the router in the API.

This keeps every feature independent and easy to maintain.

---

# Running Tests

```bash
pytest
```

With coverage

```bash
pytest --cov=app
```

---

# Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

---

# Code Quality

Format

```bash
black .
```

Lint

```bash
ruff check .
```

Sort imports

```bash
isort .
```

---

# Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- Alembic
- PostgreSQL
- Uvicorn
- Docker
- Pytest

---

# Best Practices

- Modular architecture
- Dependency Injection
- Environment-based configuration
- Repository Pattern
- Service Layer
- Type hints
- Pydantic validation
- Async support
- API versioning
- Centralized exception handling

---

# Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# License

This project is licensed under the MIT License.

---

## Author

**Nikhil Pandey**

GitHub: https://github.com/NikhilRPandey1
