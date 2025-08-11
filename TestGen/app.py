from flask import Flask, request, jsonify, send_from_directory
import requests
import os
import json

app = Flask(__name__, template_folder="templates")

# ====== Serve UI ======
@app.route("/")
def home():
    return send_from_directory("templates", "index.html")


# ====== Detect Ollama host ======
def get_ollama_url():
    possible_hosts = [
        "http://localhost:11434",
        "http://127.0.0.1:11434",
        "http://host.docker.internal:11434"  # for Docker
    ]
    for host in possible_hosts:
        try:
            r = requests.get(f"{host}/api/tags", timeout=2)
            if r.status_code == 200:
                return host
        except:
            continue
    return None


# ====== Endpoint to list Ollama models ======
@app.route("/ollama/models", methods=["GET"])
def ollama_models():
    base_url = get_ollama_url()
    if not base_url:
        return jsonify({"error": "Could not reach Ollama. Is it running?"}), 500
    try:
        r = requests.get(f"{base_url}/api/tags", timeout=5)
        r.raise_for_status()
        data = r.json()
        models = [m["name"] for m in data.get("models", [])]
        return jsonify({"models": models})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ====== /generate stays as you had ======
@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    code = data.get("code", "")
    language = data.get("language", "python")
    framework = data.get("framework", "")
    provider = data.get("provider", "openai").lower()
    api_key = data.get("api_key", "").strip()
    model = data.get("model", "").strip()
    ollama_model = data.get("ollama_model", "").strip()

    if not code:
        return jsonify({"error": "No code provided"}), 400

    prompt = f"Generate unit tests in {language} using {framework or 'an appropriate test framework'} for the following code:\n\n{code}"

    try:
        if provider == "ollama":
            base_url = get_ollama_url()
            if not base_url:
                return jsonify({"error": "Could not reach Ollama"}), 500

            payload = {
                "model": ollama_model or "llama3.1",
                "prompt": prompt
            }
            res = requests.post(f"{base_url}/api/generate", json=payload)
            res.raise_for_status()

            # Streamed JSON parsing
            generated = ""
            for line in res.text.strip().split("\n"):
                try:
                    obj = json.loads(line)
                    generated += obj.get("response", "")
                except:
                    pass
            tests = generated.strip()

        elif provider == "openai":
            url = "https://api.openai.com/v1/chat/completions"
            headers = {"Authorization": f"Bearer {api_key}"}
            payload = {
                "model": model or "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "You are a code generation assistant."},
                    {"role": "user", "content": prompt}
                ]
            }
            res = requests.post(url, headers=headers, json=payload)
            res.raise_for_status()
            data = res.json()
            tests = data["choices"][0]["message"]["content"]

        elif provider == "gemini":
            gemini_model = model or "gemini-2.0-flash"
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{gemini_model}:generateContent"
            headers = {
                "Content-Type": "application/json",
                "X-goog-api-key": api_key
            }
            payload = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            res = requests.post(url, headers=headers, json=payload)
            res.raise_for_status()
            data = res.json()
            tests = data["candidates"][0]["content"]["parts"][0]["text"]

        elif provider == "openrouter":
            url = "https://openrouter.ai/api/v1/chat/completions"
            headers = {"Authorization": f"Bearer {api_key}"}
            payload = {
                "model": model or "google/gemma-7b-it",
                "messages": [
                    {"role": "system", "content": "You are a code generation assistant."},
                    {"role": "user", "content": prompt}
                ]
            }
            res = requests.post(url, headers=headers, json=payload)
            res.raise_for_status()
            data = res.json()
            tests = data["choices"][0]["message"]["content"]

        else:
            return jsonify({"error": f"Unknown provider: {provider}"}), 400

        return jsonify({"tests": tests})

    except requests.HTTPError as e:
        return jsonify({"error": str(e), "details": e.response.text}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
