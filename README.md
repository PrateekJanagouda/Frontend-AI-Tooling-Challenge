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

**Objective:**  
Develop a Node.js CLI tool or web endpoint that uses a Large Language Model (LLM) to generate tests for React components.

**Steps:**
1. **Input Handling:**  
   Accept a code snippet (React component) as input.

2. **Prompt Engineering:**  
   - Compose system and user prompts to guide the LLM.
   - Instruct the model to generate Jest + React Testing Library tests.
   - Ensure edge cases are included and only a code block is output.

3. **Execution & Output:**  
   - Run the tool on the two provided code snippets.
   - Display the raw output from the LLM.
   - Review and critique the generated tests.
   - Refine and present the final, improved test cases.

---

## Getting Started

- Clone this repository.
- Follow the instructions in the respective directories for setting up the dashboard and the AI test generator tool.

---

**Note:**  
Focus on code quality, clear documentation, and user-friendly UX/UI.  
Include comments and explanations where necessary, especially for complex data transformations and prompt logic.
