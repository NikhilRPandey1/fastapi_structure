# FastAPI Structure

A minimal, modular boilerplate showing how to organize a **FastAPI** project with async SQLAlchemy, JWT-based authentication, and a clean separation between routers, views, schemas, and models.

## ✨ Features

- ⚡ **FastAPI** with async request handling
- 🗄️ **SQLAlchemy (async)** ORM using `asyncpg` for PostgreSQL
- 🔐 **JWT authentication** (login / signup) with `passlib` (bcrypt) password hashing
- ⚙️ **Environment-based configuration** via `pydantic-settings` + `.env`
- 📦 **Feature-based module layout** — each domain (e.g. `accounts`) owns its router, views, schemas, and models
- ✅ **Pydantic** request/response validation

## Project Structure

```text
.
├── api/
│   └── accounts/                # Feature module: accounts/auth
│       ├── __init__.py
│       ├── router.py             # Registers routes -> views
│       ├── models/
│       │   └── user.py           # SQLAlchemy User model
│       ├── schemas/
│       │   └── users.py          # Pydantic request schemas (Login/Signup)
│       └── views/
│           └── auth.py           # Business logic for login/signup
│
├── core/
│   ├── config.py                  # App settings (Settings, loaded from .env)
│   └── helper.py                  # Password hashing & JWT token helpers
│
├── db/
│   ├── base.py                    # Imports Base + all models (for metadata)
│   └── session.py                 # Async engine, session factory, get_db dependency
│
├── main.py                        # FastAPI app entrypoint
└── requirements.txt
```

### How a request flows

```
Client
  │
  ▼
Router (api/accounts/router.py)
  │
  ▼
View (api/accounts/views/auth.py)  ── business logic
  │
  ▼
Schema (api/accounts/schemas/users.py) ── validation
  │
  ▼
Model (api/accounts/models/user.py) ── SQLAlchemy ORM
  │
  ▼
Database (db/session.py — async PostgreSQL via asyncpg)
```

## Tech Stack

| Category        | Library                                  |
|------------------|-------------------------------------------|
| Web framework    | FastAPI                                   |
| ASGI server      | Uvicorn                                   |
| ORM              | SQLAlchemy (async)                        |
| Database driver  | asyncpg / psycopg2                        |
| Validation       | Pydantic v2, pydantic-settings            |
| Auth             | PyJWT, passlib (bcrypt)                   |
| Config           | python-dotenv                             |

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/NikhilRPandey1/fastapi_structure.git
cd fastapi_structure
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root with the following keys (all are required by `core/config.py`):

```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/database
SECRET_KEY=your-secret-key
DEBUG=True
ALGORITHM=HS256
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

On startup, the app automatically creates all tables defined on `Base.metadata` (see `main.py`) against the configured database.

## API Documentation

Once the server is running, interactive docs are available at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Available Endpoints

All routes are mounted under the `/api` prefix.

| Method | Endpoint             | Description                  |
|--------|-----------------------|-------------------------------|
| POST   | `/api/auth/signup`    | Create a new user account     |
| POST   | `/api/auth/login`     | Authenticate and get a JWT    |

## Adding a New Module

Follow the pattern used by `api/accounts` to add a new feature (e.g. `api/products`):

```
api/<module>/
├── __init__.py
├── router.py       # APIRouter + add_api_route registrations
├── models/         # SQLAlchemy models
├── schemas/        # Pydantic request/response schemas
└── views/          # Business logic (called by router)
```

Then:

1. Import the new model in `db/base.py` so its table is included in `Base.metadata`.
2. Include the new router in `main.py`:
   ```python
   app.include_router(your_router, prefix="/api")
   ```

## License

This project is licensed under the MIT License.

## Author

**Nikhil Pandey**
GitHub: https://github.com/NikhilRPandey1
