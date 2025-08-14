from flask import Flask, render_template, request, Response, stream_with_context, jsonify
from flask_pymongo import PyMongo
from datetime import datetime
import os, json, requests, re

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/unit_test_generator"
mongo = PyMongo(app)

OLLAMA_URL = "http://localhost:11434"

# -------- Output Cleaner --------
def clean_ai_output(text):
    # Extract only first code block if triple backticks are present
    code_match = re.search(r"```(?:\w+)?\s*([\s\S]*?)\s*```", text)
    if code_match:
        code = code_match.group(1)
    else:
        code = text

    # Normalize line endings
    code = code.replace("\r\n", "\n")

    # If code is in a single line, try splitting where Python would indent
    if "\n" not in code.strip():
        code = re.sub(r"(?<=[a-zA-Z0-9]):\s+(?=def|class|@)", ":\n    ", code)
        code = re.sub(r"(?<=\))\s+(?=def|class)", "\n", code)

    # Ensure consistent indentation (convert 2+ spaces to 4 spaces)
    code = re.sub(r" {2,}", "    ", code)

    # Remove extra spaces from empty lines
    code = re.sub(r"\n\s+\n", "\n\n", code)

    return code.strip("\n")

# -------- Ollama Helpers --------
def list_ollama_models():
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags")
        if r.status_code == 200:
            return [m["name"] for m in r.json().get("models", [])]
    except:
        return []
    return []

def pull_ollama_model_stream(model_name):
    """Stream Ollama model download progress"""
    r = requests.post(f"{OLLAMA_URL}/api/pull", json={"name": model_name}, stream=True)
    for line in r.iter_lines():
        if line:
            yield f"data: {line.decode()}\n\n"

# -------- Routes --------
@app.route("/")
def index():
    history = list(mongo.db.history.find().sort("timestamp", -1))
    for h in history:
        h["_id"] = str(h["_id"])
        h["preview"] = (h["code"][:3] + "...") if h.get("code") else "N/A"
    return render_template("index.html", history=history)

@app.route("/ollama_models")
def ollama_models():
    return jsonify(list_ollama_models() or [])



@app.route("/ollama_pull")
def ollama_pull():
    model_name = request.args.get("model")
    return Response(stream_with_context(pull_ollama_model_stream(model_name)), mimetype="text/event-stream")

@app.route("/generate", methods=["GET"])
def generate():
    code = request.args.get("code", "")
    language = request.args.get("language", "")
    framework = request.args.get("framework", "")
    provider = request.args.get("provider", "")
    api_key = request.args.get("api_key", "")
    model = request.args.get("model", "")
    ollama_model = request.args.get("ollama_model", "")
    requirements = request.args.get("requirements", "")

    prompt = f"Write unit tests for the following {language} code using {framework or 'an appropriate framework'}:\n\n{code}\n\nRequirements: {requirements}\n\nReturn ONLY the unit test code, no explanations."

    def stream():
        full_output = ""
        try:
            if provider == "ollama":
                available_models = list_ollama_models()
                if ollama_model not in available_models:
                    yield f"data: __MISSING_MODEL__{ollama_model}\n\n"
                    return
                url = f"{OLLAMA_URL}/api/generate"
                payload = {"model": ollama_model, "prompt": prompt, "stream": True}
                with requests.post(url, json=payload, stream=True) as r:
                    for line in r.iter_lines():
                        if line:
                            data = json.loads(line)
                            raw_chunk = data.get("response", "")
                            chunk_text = clean_ai_output(raw_chunk)
                            full_output += chunk_text + "\n"
                            for out_line in chunk_text.splitlines():
                                yield f"data: {out_line}\n\n"

            elif provider == "openai":
                from openai import OpenAI
                client = OpenAI(api_key=api_key)
                with client.chat.completions.stream(
                    model=model or "gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                ) as s:
                    for event in s:
                        if event.type == "message.delta":
                            raw_chunk = event.delta or ""
                            chunk_text = clean_ai_output(raw_chunk)
                            full_output += chunk_text + "\n"
                            for out_line in chunk_text.splitlines():
                                yield f"data: {out_line}\n\n"

            elif provider == "gemini":
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                gemini_model = genai.GenerativeModel(model or "gemini-2.0-flash")
                for chunk in gemini_model.generate_content(prompt, stream=True):
                    raw_chunk = chunk.text or ""
                    chunk_text = clean_ai_output(raw_chunk)
                    full_output += chunk_text + "\n"
                    for out_line in chunk_text.splitlines():
                        yield f"data: {out_line}\n\n"

            elif provider == "openrouter":
                headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
                payload = {
                    "model": model or "openai/gpt-4o-mini",
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": True
                }
                with requests.post("https://openrouter.ai/api/v1/chat/completions",
                                   headers=headers, json=payload, stream=True) as r:
                    for line in r.iter_lines():
                        if line and line.startswith(b"data:"):
                            try:
                                data = json.loads(line[5:])
                                raw_chunk = data["choices"][0]["delta"].get("content", "")
                                chunk_text = clean_ai_output(raw_chunk)
                                full_output += chunk_text + "\n"
                                for out_line in chunk_text.splitlines():
                                    yield f"data: {out_line}\n\n"
                            except:
                                pass

            # Save clean output to DB
            mongo.db.history.insert_one({
                "code": code,
                "language": language,
                "framework": framework,
                "provider": provider,
                "requirements": requirements,
                "tests": clean_ai_output(full_output),
                "timestamp": datetime.now()
            })

        except Exception as e:
            yield f"data: Error: {str(e)}\n\n"

    return Response(stream_with_context(stream()), mimetype="text/event-stream")

@app.route("/history/<id>", methods=["GET"])
def get_history(id):
    from bson.objectid import ObjectId
    item = mongo.db.history.find_one({"_id": ObjectId(id)})
    if item:
        item["_id"] = str(item["_id"])
        return jsonify(item)
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
