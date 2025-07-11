import urllib

from flask import Flask, request, jsonify
from flask_cors import CORS
from llama_cpp import Llama
import os
import urllib.request

# --- Initialize Flask app ---
app = Flask(__name__)
CORS(app)  # Allow frontend (Angular) to access this API

# --- Load local GGUF model  ---
MODEL_PATH = "./models/tinyllama-1.1b-chat-v1.0.Q6_K.gguf"
MODEL_URL = 'https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q6_K.gguf'

os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

if not os.path.exists(MODEL_PATH):
    print("Downloading model...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

# Initialize LLaMA model
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=4
)

# --- Format prompt history into a conversation ---
def format_prompt(messages):
    prompt = "You are a helpful assistant.\n"
    for msg in messages:
        if msg["role"] == "user":
            prompt += f"User: {msg['content']}\n"
        elif msg["role"] == "assistant":
            prompt += f"Assistant: {msg['content']}\n"
    prompt += "Assistant:"
    return prompt

# --- Main chat endpoint ---
@app.route("/chat", methods=["POST"])
def chat():
    """
    POST /chat
    JSON body:
    {
        "messages": [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"}
        ]
    }

    Returns:
    {
        "role": "assistant",
        "content": "Response from LLaMA"
    }
    """
    data = request.json
    messages = data.get("messages", [])

    # Format messages into a single string prompt
    prompt = format_prompt(messages)

    # Generate response from LLaMA
    try:
        output = llm(
            prompt=prompt,
            max_tokens=200,
            stop=["User:", "Assistant:"],
            temperature=0.7
        )

        # Extract reply from output
        reply_text = output["choices"][0]["text"].strip()

        return jsonify({
            "role": "assistant",
            "content": reply_text
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- Run the app ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
