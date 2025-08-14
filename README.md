# Traffic Insights & AI Test Generator

This project contains two core tasks:

---

## Task 1 — Data Dashboard

**Objective:**  
Build a modern, interactive data dashboard using React (Vite preferred for speed, but CRA is also acceptable).

**Steps:**
1. **Fetch Data:**  
   Retrieve hourly traffic data from the provided API using the given curl command and API key.

2. **Data Processing:**  
   - Aggregate totals and identify peak values.
   - Calculate moving averages.
   - Detect and highlight anomalies in the data.

3. **Dashboard Features:**  
   Create an engaging dashboard with the following components:
   - **Overview Cards:** Key metrics and summary statistics.
   - **Line Chart:** Visualize trends, including upward and downward movements.
   - **Stacked Bar/Area Chart:** Show detailed breakdowns (e.g., by category or time).
   - **Hourly Heatmap:** Highlight traffic intensity by hour.
   - **Peak Hour Highlights:** Emphasize periods of highest activity.
   - **Anomaly List:** Clearly display detected anomalies.

---

## Task 2 — AI Test Generator

## Objective
Build a **Flask-based web app** that uses multiple Large Language Model (LLM) providers to automatically generate **unit tests** for any given code snippet — supporting Python, JavaScript, Java, Go, Ruby, and more — with optional test framework selection.

---

##  Steps

### 1. Input Handling
- Accept a **code snippet** via a modern web UI.
- Allow selection of:
  - Programming language
  - Test framework (optional)
  - LLM provider (OpenAI, Google Gemini, OpenRouter, Ollama)
  - Model name (when applicable)
  - API key (for cloud providers)

### 2.  Prompt Engineering
- Craft **system** and **user** prompts to instruct the LLM to:
  - Generate unit tests in the chosen language.
  - Use the selected test framework, or pick an appropriate default.
  - Ensure test coverage includes **edge cases** and realistic scenarios.
  - Output **only** the complete test file code.

### 3.  Execution & Output
- Send the prompt and input data to the selected LLM provider:
  - **OpenAI** via `chat/completions`
  - **Google Gemini** via `generateContent`
  - **OpenRouter** for free or paid models
  - **Ollama** for local models (e.g., LLaMA, Mistral, etc.)
- Display the generated tests in a formatted code block within the UI.
- Provide a **copy-to-clipboard** option for convenience.


### 5.  Final Deliverable
- A **professional, modern web interface** that enables developers to paste code and instantly receive high-quality unit tests from their chosen LLM.
- Clean, maintainable Flask backend with clear API endpoints for `/generate` and `/ollama/models`.
  
---

## Getting Started

- Clone this repository.
- Follow the instructions in the respective directories for setting up the dashboard and the AI test generator tool.

---


