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
