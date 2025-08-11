# 🧪 TestGen — AI-Powered Unit Test Generator

Generate **high-quality unit tests** for your code instantly using **OpenAI**, **Google Gemini**, **Ollama**, or **OpenRouter** — all from a clean, modern web interface.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-yellow)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-blue)

---



---

## 📂 Project Structure
```
TestGen/
├── templates/
     ├──index.html
├── app.py
```

---

## ⚡ Quick Start
---

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/PrateekJanagouda/Frontend-AI-Tooling-Challenge.git
cd TestGen
```

2️⃣ Install Dependencies
```
pip install flask requests
```

3️⃣ Run the Application
```
python app.py
```
By default app runs on : 
```
http://127.0.0.1:5000
```
               or

Open in browser :    http://localhost:5000


---


🔌 API Endpoints
GET /ollama/models
Returns locally available Ollama models.

json
Copy
Edit
{ "models": ["llama2", "mistral", ...] }
POST /generate
Generates unit tests from a code snippet.

Request:

json
Copy
Edit
{
  "code": "def add(a,b): return a+b",
  "language": "python",
  "framework": "pytest",
  "provider": "openai",
  "api_key": "YOUR_API_KEY",
  "model": "gpt-4o-mini",
  "ollama_model": ""
}
Response:

json
Copy
Edit
{
  "tests": "def test_add():\n    assert add(2,3) == 5\n..."
}
🔧 Supported Providers
Provider	API Key Required	Notes
OpenAI	✅	GPT models (gpt-4o-mini, etc.)
Gemini	✅	gemini-2.0-flash by default
Ollama	❌	Runs locally; detects models automatically
OpenRouter	✅	Supports multiple free/paid models

📜 Prompt Template
text
Copy
Edit
Generate unit tests in {language} using {framework or 'an appropriate test framework'} for the following code:

{code}

Requirements:
- Include both normal and edge-case coverage
- Use descriptive test names
- Output only the test code
📸 Screenshot
(Insert screenshot of the UI here)

🤝 Contributing
Fork the repo

Create a new branch (feature/your-feature)

Commit your changes

Open a Pull Request

📄 License
This project is licensed under the MIT License.

💡 Tip
Want to run locally without API keys? Install Ollama and pull a model:

bash
Copy
Edit
ollama pull llama2
Then select Ollama in the UI.

yaml
Copy
Edit

---

I kept this **minimal, professional, and GitHub-friendly** while still showing all necessary info.  
If you want, I can also make a **fancier README with a banner image and visual UI
