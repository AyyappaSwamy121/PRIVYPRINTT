# PRIVYPRINTT

Sprint A scaffolding for Privy (privacy-first document platform) with:
- Django 5 backend (`backend/`)
- Next.js 14 frontend (`frontend/`)

## Backend (Django)
```bash
cd backend
python -m pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Backend API basics:
- Admin: `http://localhost:8000/admin/`
- Health: `http://localhost:8000/api/health/`
- JWT token: `POST http://localhost:8000/api/auth/token/`
- JWT refresh: `POST http://localhost:8000/api/auth/token/refresh/`

## Frontend (Next.js)
```bash
cd frontend
cp .env.example .env.local
npm install
npm run dev
```

Frontend runs at `http://localhost:3000` and points to `http://localhost:8000/api` by default.

## Sprint B placeholders
Model/business logic, endpoint implementations, refresh-token automation, encryption/storage workflows, and domain-specific modules are intentionally left as TODO placeholders for Sprint B.
