# FastAPI Auth API 🔒

A **production-ready FastAPI backend** implementing JWT-based authentication with hashed secrets, access & refresh tokens, and protected endpoints. Ready to deploy, test, and integrate.

---

## Features ✅

- JWT-based authentication (access + refresh tokens)  
- Hashed client secrets for security (no plain text)  
- Token expiry: short-lived access, longer refresh  
- Protected endpoints (`/me`, `/secure-data`)  
- Environment variable support via `.env`  
- Test user auto-created for immediate testing  
- Fully compatible with **curl**, **Postman**, and GitHub deployment  

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

---

