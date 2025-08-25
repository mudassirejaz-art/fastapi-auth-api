# FastAPI Auth API 🔒

A **production-ready FastAPI backend** implementing JWT-based authentication with hashed secrets, access & refresh tokens, and protected endpoints. Ready to deploy, test, and integrate.

---

## Features ✅

* JWT-based authentication (access + refresh tokens)
* Hashed client secrets for security (no plain text)
* Token expiry: short-lived access, longer refresh
* Protected endpoints (`/me`, `/secure-data`)
* Environment variable support via `.env`
* Test user auto-created for immediate testing
* Fully compatible with **curl**, **Postman**, and GitHub deployment

---

## Project Structure 📂

fastapi-auth-api/
├─ app/
│ ├─ main.py # FastAPI app entry point
│ ├─ models.py # SQLAlchemy models
│ ├─ schemas.py # Pydantic schemas
│ ├─ auth.py # Authentication & JWT logic
│ ├─ deps.py # Dependency overrides (DB/session)
│ └─ crud.py # CRUD functions
├─ .env.example # Example environment variables
├─ requirements.txt # Python dependencies
└─ README.md # This file

---

## Setup & Installation 🛠️

1. **Clone the repository**

```bash
git clone https://github.com/mudassirejaz-art/fastapi-auth-api.git
cd fastapi-auth-api
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Copy `.env.example` to `.env` and update as needed:

```
SECRET_KEY=your_jwt_secret
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_MINUTES=1440
DATABASE_URL=sqlite:///./app.db
```

5. **Run the application**

```bash
uvicorn app.main:app --reload
```

Server will run at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## API Endpoints 🖥️

**Auth**

* `POST /login` — Login with `client_key` and `secret_key` to get access & refresh tokens
* `POST /refresh` — Use refresh token to get a new access token

**Protected**

* `GET /me` — Get current user info (requires Bearer token)
* `GET /secure-data` — Example protected resource

**Test User**

A test user is auto-created on startup:

```json
{
  "client_key": "myclient123",
  "secret_key": "mysecret456"
}
```

## Testing Examples ⚡

**Login:**

```bash
curl -X POST http://127.0.0.1:8000/login \
-H "Content-Type: application/json" \
-d '{"client_key": "myclient123", "secret_key": "mysecret456"}'
```

**Access Protected Endpoint:**

```bash
curl -H "Authorization: Bearer <ACCESS_TOKEN>" http://127.0.0.1:8000/me
```

## Deployment Tips 🚀

* Use Docker for containerized deployment
* Set production environment variables
* Use a proper DB (PostgreSQL/MySQL) instead of SQLite for production

## License 📄

This project is open-source and available under the MIT License.
