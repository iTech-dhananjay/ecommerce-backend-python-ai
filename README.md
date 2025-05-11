## 🛠️ Project Setup Steps
Follow these steps to run your FastAPI backend project locally using Docker.

### 📁 1. Clone the repository or navigate to your created directory
```bash
cd ecommerce-backend
```

### 🐳 2. Start PostgreSQL and FastAPI using Docker
```bash
docker-compose up --build
```

This will:
- Start a Postgres database
- Start FastAPI server at `http://localhost:8000`

### ⚙️ 3. Install Python packages (optional - for local dev)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### ⚒️ 4. Initialize Alembic and apply DB migrations
```bash
alembic upgrade head
```

> Make sure you’ve configured `alembic.ini` with your DB connection from `.env`

### 🌱 5. Seed development data (users/products)
```bash
python scripts/seed_data.py
```

This will:
- Create superadmin/admin/user accounts
- Generate fake users and products using `faker`

### 🔑 6. Access Swagger API Docs with Auth
```bash
http://localhost:8000/docs
```
- Add your `JWT token` in the top-right authorize button to access protected routes

## 👨‍💻 Developer Notes

### 🔁 Run tests
```bash
pytest tests/
```

### ♻️ Format & Lint (Optional)
```bash
pip install black isort flake8
black . && isort . && flake8
```

## 📦 Project Stack
- **FastAPI** (API Framework)
- **PostgreSQL** (Database)
- **SQLAlchemy + Alembic** (ORM + Migrations)
- **JWT Auth** (OAuth2 password flow)
- **Stripe** (Payment Integration)
- **OpenAI / Whisper** (AI endpoints)
- **Docker** (Local environment)
- **GitHub Actions** (CI/CD pipeline)
- **Faker** (Seeding fake data)

## ✅ Default Admin Credentials
- `superadmin@example.com` / `super123`
- `admin@example.com` / `admin123`
- `user@example.com` / `user123`
