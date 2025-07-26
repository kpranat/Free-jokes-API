
# 😂 Free Jokes API

## ⚡ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/free-jokes-api.git
cd free-jokes-api

# 2. Install required Python packages
pip install -r requirements.txt

# 3. Run the Flask app
python app.py

# Access it at:
# http://localhost:5000/jokes
```


A simple and fun **Flask-based API** that lets users view and add jokes.  
Deployed live at 👉 [https://free-jokes-api.onrender.com](https://free-jokes-api.onrender.com)

---

## 🔥 Features

- ✅ GET & POST endpoints
- ✅ JSON response format
- ✅ Rate-limited: 10 requests per minute per IP
- ✅ Easy deployment (Render-ready)
- ✅ In-memory joke storage

---

## 📡 Live API Endpoints

### `GET /jokes`

Returns all available jokes:

📌 Example:  
```bash
curl https://free-jokes-api.onrender.com/jokes
```

📥 Sample Response:
```json
{
  "jokes": [
    {
      "id": "J001",
      "setup": "Why do programmers prefer dark mode?",
      "punchline": "Because light attracts bugs!"
    },
    ...
  ]
}
```

---

### `POST /jokes`

Add a new joke. Only `punchline` is required.

📌 Example:
```bash
curl -X POST https://free-jokes-api.onrender.com/jokes \
-H "Content-Type: application/json" \
-d '{"setup": "Why did the tomato blush?", "punchline": "Because it saw the salad dressing."}'
```

📥 Sample Response:
```json
{
  "message": "New joke added"
}
```

---

## 🚫 Rate Limit

To prevent spam, each IP is limited to:

```
🔁 10 requests per minute
```

---

## 🛠️ Local Development

### 1. Clone this repo

```bash
git clone https://github.com/yourusername/free-jokes-api.git
cd free-jokes-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run locally

```bash
python app.py
```

Go to: `http://localhost:5000/jokes`

---

## 🚀 Deployment on Render

1. Push to GitHub
2. Go to [https://render.com](https://render.com)
3. Create **New Web Service**
4. Fill:

| Setting         | Value                          |
|----------------|--------------------------------|
| Build Command  | `pip install -r requirements.txt` |
| Start Command  | `gunicorn app:app`             |
| Runtime        | Python 3.x                     |

✅ Done! Render gives you a public link.

---

## 📁 Project Structure

```
free-jokes-api/
├── app.py              # Flask API logic
├── requirements.txt    # Python packages
├── Procfile            # Render start command
└── runtime.txt         # Python version
```

---

## 📃 Dependencies

- Flask
- flask-limiter
- gunicorn

Install with:
```bash
pip install -r requirements.txt
```

---

## 📄 License

MIT License — use it freely!

---

## 👋 Try It Live!

▶️ [https://free-jokes-api.onrender.com/jokes](https://free-jokes-api.onrender.com/jokes)
