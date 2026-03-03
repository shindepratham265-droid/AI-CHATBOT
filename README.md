# 🤖 AI-CHATBOT
### Conversational AI Chatbot — Powered by Google Gemini 1.5 Flash

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-Framework-lightgrey?style=flat-square&logo=flask)
![Gemini](https://img.shields.io/badge/Gemini-1.5%20Flash-orange?style=flat-square&logo=google)

> A lightweight Flask chatbot with conversation memory, token management, and a clean web UI.

---

## ✨ Features
- 🧠 Remembers last 6 messages for natural conversation
- ✂️ Trims long inputs to avoid token waste
- 📅 Injects today's date into every prompt automatically
- 🔑 API key secured via `.env` file
- 🌐 REST API + built-in browser UI

---

## 🚀 Quick Start
```bash
pip install flask flask-cors google-generativeai python-dotenv
echo "GEMINI_API_KEY=your_key_here" > .env
python chatbot.py
```
Then open `http://localhost:5000`

> Get a free API key at https://aistudio.google.com

---

## ⚙️ Configuration
| Setting | Default | Purpose |
|---|---|---|
| `MAX_INPUT_CHARS` | 1500 | Max user message length |
| `MAX_HISTORY_MESSAGES` | 6 | Conversation memory |
| `MAX_OUTPUT_TOKENS` | 200 | Max reply length |

---

## 📡 API
**POST** `/chat`
```json
Request:  { "message": "Hello!" }
Response: { "reply": "Hi! How can I help?", "tokens_est": 45 }
```

---

## 🛡️ Security
- API key stored in `.env` — never hardcoded
- Input trimmed to prevent prompt injection
- History capped — memory never grows unbounded

> ⚠️ History is in-memory and resets on server restart. Single-user only.

---

## 📁 Project Structure
```
AI-CHATBOT/
├── chatbot.py          # Main Flask app
├── requirements.txt    # Dependencies
├── .env                # API key (hidden from GitHub)
└── templates/
    └── frontend.html   # Chat UI
```
```
