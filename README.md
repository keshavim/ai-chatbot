# 🧠 AI Chatbot Backend (LLaMA + Flask + Docker)

This is a simple local AI chatbot backend powered by [LLaMA](https://github.com/ggerganov/llama.cpp) using `llama-cpp-python`. It runs a GGUF model and exposes a `/chat` API using Flask, packaged in Docker for easy use.

---

## 🚀 How to Run

### 1. 🧱 Build the Docker Image

From inside the `backend/` folder:

```bash
docker build -t backend .
```

### 2. ▶️ Run the Container

Replace the model path if needed:

```bash
docker run -p 5000:5000 -v "$PWD/models:/app/models" backend
```

> Make sure `models/` contains your `.gguf` model file.

---

### 3. 🧪 Test the API

In a second terminal, send a POST request:

```bash
curl -X POST http://localhost:5000/chat \
-H "Content-Type: application/json" \
-d '{
  "messages": [
    {"role": "user", "content": "What is machine learning?"}
  ]
}'
```

You’ll get a response from the LLaMA model:

```json
{
  "role": "assistant",
  "content": "Machine learning is a field of artificial intelligence..."
}
```

---

That’s it! You're running a local LLaMA-based AI backend.
