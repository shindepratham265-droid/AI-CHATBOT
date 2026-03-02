from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from google import genai
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# ---------- CONFIG ----------
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-1.5-flash"

MAX_INPUT_CHARS = 1500
MAX_HISTORY_MESSAGES = 6
MAX_OUTPUT_TOKENS = 200
# ----------------------------

app = Flask(__name__)
CORS(app)

client = genai.Client(api_key=API_KEY)

# Store conversation
conversation_history = []


# ---------- HELPERS ----------

def estimate_tokens(text):
    return len(text) // 4


def trim_text(text, max_chars):
    return text[:max_chars] if len(text) > max_chars else text


def trim_history(history):
    if len(history) > MAX_HISTORY_MESSAGES:
        return history[-MAX_HISTORY_MESSAGES:]
    return history


# -----------------------------


@app.route("/")
def home():
    return render_template("frontend.html")


@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history

    # Dynamic system prompt with real date
    current_date = datetime.now().strftime("%A, %B %d, %Y")
    SYSTEM_PROMPT = (
        f"You are a helpful assistant. "
        f"Today's date is {current_date}. "
        "Always give short, clear, and direct answers. "
        "Avoid long explanations unless asked."
    )

    data = request.get_json()
    user_input = data.get("message", "")

    user_input = trim_text(user_input, MAX_INPUT_CHARS)

    conversation_history.append(f"User: {user_input}")
    conversation_history = trim_history(conversation_history)

    full_prompt = SYSTEM_PROMPT + "\n\n" + "\n".join(conversation_history)

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=full_prompt,
            config={
                "max_output_tokens": MAX_OUTPUT_TOKENS
            }
        )

        reply = response.text if response.text else "No response"

        conversation_history.append(f"Assistant: {reply}")

        return jsonify({
            "reply": reply,
            "tokens_est": estimate_tokens(full_prompt)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=False)