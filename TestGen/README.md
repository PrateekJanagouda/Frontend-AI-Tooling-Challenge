# 🧪 TestGen — AI-Powered Unit Test Generator

Generate **high-quality unit tests** for your code instantly using **OpenAI**, **Google Gemini**, **Ollama**, or **OpenRouter** — all from a clean, modern web interface.

## ✨ Features

- **Multiple AI Providers** — switch between OpenAI, Gemini, Ollama, and OpenRouter.
- **Real-Time Streaming** — see generated tests appear line-by-line.
- **Persistent History** — all generations stored in MongoDB with timestamps.
- **Ollama Model Management** — list and pull local Ollama models from the UI.
- **Automatic Output Cleaning** — ensures clean, ready-to-run code.
- **Responsive UI** — sidebar history, dark/light friendly.


![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-yellow)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-blue)

---

## 📂 Project Structure

```
TestGen/
├── templates/
│   └── index.html
├── app.py
```

---

## ⚡ Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/PrateekJanagouda/Frontend-AI-Tooling-Challenge.git
cd Frontend-AI-Tooling-Challenge/TestGen
```

### 2️⃣ Install Dependencies

```bash
pip install flask requests
```

### 3️⃣ Run the Application

```bash
python app.py
```

By default, the app runs on:

```
http://127.0.0.1:5000
```
or

Open in browser: 
```
[http://localhost:5000](http://localhost:5000)
```

---

## 🔌 API Endpoints

### `GET   /ollama/models`
```
http://localhost:5000/ollama/models
```
Returns locally available Ollama models.

**Response:**
```json
{ "models": ["llama2", "mistral", ...] }
```

---

### `POST /generate`

Generates unit tests from a code snippet.

**Request:**
```json
{
  "code": "def add(a,b): return a+b",
  "language": "python",
  "framework": "pytest",
  "provider": "openai",
  "api_key": "YOUR_API_KEY",
  "model": "gpt-4o-mini",
  "ollama_model": ""
}
```

**Response:**
```json
{
  "tests": "def test_add():\n    assert add(2,3) == 5\n..."
}
```

---

## 🔧 Supported Providers

| Provider    | API Key Required | Notes                                        |
|-------------|:---------------:|----------------------------------------------|
| OpenAI      |      ✅         | GPT models (gpt-4o-mini, etc.)               |
| Gemini      |      ✅         | gemini-2.0-flash by default                  |
| Ollama      |      ❌         | Runs locally; detects models automatically   |
| OpenRouter  |      ✅         | Supports multiple free/paid models           |

---

## 📜 Prompt Template

```
Generate unit tests in {language} using {framework or 'an appropriate test framework'} for the following code:

{code}

Requirements:
- Include both normal and edge-case coverage
- Use descriptive test names
- Output only the test code
```

---



##  Example 1

As an example Gemini-2.0-flash has been considered 

In order to test we have taken the below JavaScript Code 

source to the example code can be downloaded from [here](https://github.com/PrateekJanagouda/Frontend-AI-Tooling-Challenge/blob/main/TestGen/examples/example1.js)


<img width="1083" height="625" alt="image" src="https://github.com/user-attachments/assets/a06c53f6-b202-4af7-8980-65f41a67c8c5" />





---

## 1 . Gemini with Google studio's Free API key and the Raw output for this is 


Raw output of the example code can be found [here](https://github.com/PrateekJanagouda/Frontend-AI-Tooling-Challenge/blob/main/TestGen/examples/example1_output.js)

---

##  Example 2

Here is the Second example [here](https://github.com/PrateekJanagouda/Frontend-AI-Tooling-Challenge/blob/main/TestGen/examples/example2.js)


## 2 . Gemini with Google studio's Free API key and the Raw output for this is 


Raw output of the example code can be found [here](https://github.com/PrateekJanagouda/Frontend-AI-Tooling-Challenge/blob/main/TestGen/examples/example2_output.js)

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch (`feature/your-feature`)
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Tip

Want to run locally without API keys? Install Ollama and pull a model:

```bash
ollama pull llama3.1
```

Then select Ollama in the UI.

---

I kept this **minimal, professional, and GitHub-friendly** while still showing all necessary info.  
If you want, I can also make a **fancier README with a banner image and visual UI**!
