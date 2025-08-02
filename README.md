## 🐳 Docker Compose Workflow

Use the following steps to clean, build, and run the app using Docker Compose.

### 🧹 1. Clean up any previous Docker state

```bash
docker compose down --volumes --remove-orphans
```

### 🔨 2. Rebuild images from scratch (no cache)
```bash
docker compose build --no-cache
```

### ▶️ 3. Start the application
```bash
docker compose up
```
The backend will be available at: http://localhost:5000
The frontend (Angular app) will be at: http://localhost:4200


💻 Manual (No Docker) Workflow

Use the following steps to run the app manually without Docker.
🧹 1. Clean any old virtual environments or node_modules

Optional but recommended before fresh setup:

rm -rf backend/venv frontend/node_modules frontend/dist

📦 2. Install dependencies
Backend (Python Flask API)

cd backend

# (Optional) Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required Python packages
pip install --upgrade pip
pip install -r requirements.txt

Frontend (Angular App)

Open a new terminal:

cd frontend

# Install Angular dependencies
npm install

▶️ 3. Start the application
Start the backend server

cd backend
source venv/bin/activate  # If not already activated
python app.py

    The backend will be available at: http://localhost:5000

Start the frontend dev server

In a new terminal:

cd frontend
ng serve

    The frontend (Angular app) will be available at: http://localhost:4200
