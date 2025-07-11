# 🧠 AI Chatbot Backend (LLaMA + Flask + Docker)

This is a simple local AI chatbot backend powered by [LLaMA](https://github.com/ggerganov/llama.cpp) using `llama-cpp-python`.  
It runs a GGUF model and exposes a `/chat` API using Flask, packaged in Docker for easy use.

---

## 🚀 How to Run

### Option 1: Using Docker (Recommended)

#### 1. 🧱 Build the Docker Image

From inside the `backend/` folder, run:

```bash
docker build -t backend .

2. ▶️ Run the Container

Make sure your local models/ folder contains your .gguf model file. Then run:

docker run -p 5000:5000 -v "$PWD/models:/app/models" backend

This command:

    Maps port 5000 inside the container to your local port 5000

    Mounts your local models/ folder into the container so the model file is accessible

3. 🧪 Test the API

In another terminal, test with:

curl -X POST http://localhost:5000/chat \
-H "Content-Type: application/json" \
-d '{
  "messages": [
    {"role": "user", "content": "What is machine learning?"}
  ]
}'

You’ll get a JSON response from the LLaMA model.
Option 2: Run Locally without Docker
Prerequisites

    Python 3.10+

    pip package manager

    Your .gguf model file in models/ folder

1. Create and activate a virtual environment (recommended)

python3 -m venv venv
source venv/bin/activate

2. Install dependencies

From the backend/ folder:

pip install --upgrade pip
pip install -r requirements.txt

3. Run the Flask app

Make sure your model is at ./models/tinyllama-1.1b-chat-v1.0.Q6_K.gguf or update MODEL_PATH in app.py.

Then run:

python app.py

The backend will start on http://localhost:5000.
4. Test the API

Same as Docker, use the curl command above to test.
