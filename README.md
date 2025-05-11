## 🛠️ Project Setup (macOS/Linux)
This project runs the **Python app locally** and **PostgreSQL via Docker**.

---

### ✅ 1. Prerequisites
Install the following:
```bash
python3 --version
pip3 --version
docker --version
docker-compose --version
```

---

### 📁 2. Create Python virtual environment & install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 🐳 3. Start PostgreSQL container via Docker
```bash
docker compose up -d
```
> ✅ This builds and runs Postgres using env vars from `.env`

Check container:
```bash
docker ps
```

To stop it:
```bash
docker-compose down
```

> 🧠 **You do NOT need to build the Docker image for the app** because you are running the Python app locally. You only use Docker for the DB.

---

### ⚙️ 4. Apply Alembic migrations
```bash
alembic upgrade head
```

---

### 🌱 5. Seed database with fake users/products
```bash
python scripts/seed_data.py
```

---

### 🚀 6. Run FastAPI app locally
```bash
uvicorn app.main:app --reload
```
Then open:
- Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## ✅ Common Commands
| Task                         | Command                              |
|------------------------------|--------------------------------------|
| Activate Python venv         | `source venv/bin/activate`           |
| Start PostgreSQL (Docker)    | `docker-compose up -d`               |
| Run Alembic migrations       | `alembic upgrade head`               |
| Seed DB with test data       | `python scripts/seed_data.py`        |
| Start FastAPI app            | `uvicorn app.main:app --reload`      |
| Stop PostgreSQL              | `docker-compose down`                |

---

## 📦 Stack Overview
- FastAPI (Backend)
- PostgreSQL (Database)
- Alembic (Migrations)
- Docker (DB only)
- Uvicorn (App Server)
- Stripe, OpenAI (Integrations)
- Faker (Seed Data)

---

## 👥 Default Test Users
| Role        | Email                  | Password   |
|-------------|------------------------|------------|
| Super Admin | superadmin@example.com | super123   |
| Admin       | admin@example.com      | admin123   |
| User        | user@example.com       | user123    |

---
