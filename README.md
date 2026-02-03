# Inventario MVP (FastAPI + React)

Rápido scaffold para una app de inventario con:
- Backend: FastAPI + SQLModel (SQLite)
- Frontend: React (Vite) + Tailwind
- Docker + docker-compose para levantar todo fácilmente
- Endpoints CRUD y autenticación JWT simple
- Endpoints opcionales de IA usando OpenAI (configura OPENAI_API_KEY)

Requisitos
- Docker & docker-compose (recomendado), o Python 3.11 + Node 18

Arranque rápido con Docker
1. Copia el repo a tu máquina.
2. Edita `backend/.env.example` y configura `JWT_SECRET`, `ADMIN_PASS`, y (opcional) `OPENAI_API_KEY`.
3. Renombra o copia a `.env` si lo deseas.
4. Desde la raíz ejecuta:
   docker-compose up --build

- Backend: http://localhost:8000
- Frontend: http://localhost:5173

Ejecución local sin Docker (opción)
Backend:
  cd backend
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  export DATABASE_URL="sqlite:///./data/inventory.db"
  uvicorn app.main:app --reload --port 8000

Frontend:
  cd frontend
  npm install
  npm run dev

Autenticación
- Token: POST /auth/token con form-data `username` y `password` (usa ADMIN_USER/ADMIN_PASS del .env)
- No implementé protección por ruta en todos los endpoints (MVP). Si quieres, la añado (dependencias y roles).

IA (opcional)
- Activa `OPENAI_API_KEY` en el .env para habilitar `/ai/ask` (ejemplo simple). Es experimental y está pensado para prototipado.

Siguientes pasos que puedo hacer ahora
- Añadir protección JWT en endpoints de productos y rutas en frontend.
- Añadir subida/almacenamiento de imágenes y lectura de barcode/Cámara.
- Implementar búsqueda semántica con embeddings y un índice simple.
- Mejorar UI/UX y agregar paginación, filtros y roles de usuario.
- Subir estos archivos a un repo de GitHub si quieres.

---