# 🧪 TestGen — AI-Powered Unit Test Generator

Generate **high-quality unit tests** for your code instantly using **OpenAI**, **Google Gemini**, **Ollama**, or **OpenRouter** — all from a clean, modern web interface.

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

## 📸 Screenshot

<img width="1912" height="934" alt="image" src="https://github.com/user-attachments/assets/0d8b12a0-b650-4e1d-af06-d2834d5328c6" />
above image shows the UI 

##  Example 1

For the purpose of example we have taken Gemini and Ollama with llama3.1 latest
In odrer to test we have taken the below React Code
```
import React, { useState } from 'react';
const QuizGameWidget = () => {
 const questions = [
 { q: 'Capital of France?', a: 'Paris' },
 { q: '2 + 2 * 2?', a: '6' },
 { q: 'Largest ocean?', a: 'Pacific' }
 ];
 const [index, setIndex] = useState(0);
 const [answer, setAnswer] = useState('');
 const [score, setScore] = useState(0);
 const [history, setHistory] = useState([]);
 const submitAnswer = () => {
 if (answer.trim() !== '') {
 const correct = questions[index].a.toLowerCase() ===
answer.trim().toLowerCase();
 setHistory([...history, { question: questions[index].q, correct }]);
 if (correct) setScore(score + 1);
 setIndex(index + 1);
 setAnswer('');
 }
 };
 return (
 <div style={{ padding: 24, width: 400, border: '1px solid #999' }}>
 <h2>Quick Quiz</h2>
 {index < questions.length ? (
 <>
 <p><strong>{questions[index].q}</strong></p>
 <input
 value={answer}
 onChange={(e) => setAnswer(e.target.value)}
 placeholder="Your answer"
 style={{ width: '100%' }}
 />
 <button onClick={submitAnswer} style={{ marginTop: 10 }}>Submit</button>
 </>
 ) : (
 <>
 <h3>Quiz Complete!</h3>
 <p>Score: {score} / {questions.length}</p>
 <ul>
 {history.map((h, i) => (
 <li key={i} style={{ color: h.correct ? 'green' : 'red' }}>
 {h.question} — {h.correct ? '✅' : '❌'}
 </li>
 ))}
 </ul>
 </>
 )}
 </div>
 );
};
export default QuizGameWidget;

```

1 . Gemini with Google studio's Free API key and the Raw output for this is 

```

```javascript
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import QuizGameWidget from './QuizGameWidget'; // Adjust the path if necessary

describe('QuizGameWidget', () => {
  test('renders the initial question', () => {
    render(<QuizGameWidget />);
    expect(screen.getByText('Capital of France?')).toBeInTheDocument();
    expect(screen.getByPlaceholderText('Your answer')).toBeInTheDocument();
    expect(screen.getByText('Submit')).toBeInTheDocument();
  });

  test('updates the answer state on input change', () => {
    render(<QuizGameWidget />);
    const inputElement = screen.getByPlaceholderText('Your answer');
    fireEvent.change(inputElement, { target: { value: 'Paris' } });
    expect(inputElement.value).toBe('Paris');
  });

  test('submits the correct answer and advances to the next question', () => {
    render(<QuizGameWidget />);
    const inputElement = screen.getByPlaceholderText('Your answer');
    const submitButton = screen.getByText('Submit');

    fireEvent.change(inputElement, { target: { value: 'Paris' } });
    fireEvent.click(submitButton);

    expect(screen.getByText('2 + 2 * 2?')).toBeInTheDocument();
    expect(inputElement.value).toBe(''); // Input should be cleared
  });

  test('submits the incorrect answer and advances to the next question', () => {
    render(<QuizGameWidget />);
    const inputElement = screen.getByPlaceholderText('Your answer');
    const submitButton = screen.getByText('Submit');

    fireEvent.change(inputElement, { target: { value: 'London' } });
    fireEvent.click(submitButton);

    expect(screen.getByText('2 + 2 * 2?')).toBeInTheDocument();
    expect(inputElement.value).toBe(''); // Input should be cleared
  });

  test('increments the score when the answer is correct', () => {
    render(<QuizGameWidget />);
    const inputElement = screen.getByPlaceholderText('Your answer');
    const submitButton = screen.getByText('Submit');

    fireEvent.change(inputElement, { target: { value: 'Paris' } });
    fireEvent.click(submitButton);

    fireEvent.change(inputElement, { target: { value: '6' } });
    fireEvent.click(submitButton);

    fireEvent.change(inputElement, { target: { value: 'Pacific' } });
    fireEvent.click(submitButton);

    expect(screen.getByText('Quiz Complete!')).toBeInTheDocument();
    expect(screen.getByText('Score: 3 / 3')).toBeInTheDocument();
  });

  test('displays the correct history at the end of the quiz', () => {
    render(<QuizGameWidget />);
    const inputElement = screen.getByPlaceholderText('Your answer');
    const submitButton = screen.getByText('Submit');

    fireEvent.change(inputElement, { target: { value: 'Paris' } });
    fireEvent.click(submitButton);

    fireEvent.change(inputElement, { target: { value: '5' } });  // Incorrect answer
    fireEvent.click(submitButton);

    fireEvent.change(inputElement, { target: { value: 'Pacific' } });
    fireEvent.click(submitButton);


    expect(screen.getByText('Quiz Complete!')).toBeInTheDocument();

    const historyItems = screen.getAllByRole('listitem');
    expect(historyItems).toHaveLength(3);
    expect(historyItems[0]).toHaveTextContent('Capital of France? — ✅');
    expect(historyItems[0]).toHaveStyle({ color: 'green' });
    expect(historyItems[1]).toHaveTextContent('2 + 2 * 2? — ❌');
    expect(historyItems[1]).toHaveStyle({ color: 'red' });
    expect(historyItems[2]).toHaveTextContent('Largest ocean? — ✅');
    expect(historyItems[2]).toHaveStyle({ color: 'green' });
  });

  test('handles empty answer submission', () => {
    render(<QuizGameWidget />);
    const inputElement = screen.getByPlaceholderText('Your answer');
    const submitButton = screen.getByText('Submit');

    fireEvent.change(inputElement, { target: { value: '' } });
    fireEvent.click(submitButton);
    expect(screen.getByText('Capital of France?')).toBeInTheDocument();  //Stays on the same question

  });

  test('Handles case-insensitive correct answers', () => {
      render(<QuizGameWidget />);
      const inputElement = screen.getByPlaceholderText('Your answer');
      const submitButton = screen.getByText('Submit');

      fireEvent.change(inputElement, { target: { value: 'pArIs' } }); // mixed-case correct answer
      fireEvent.click(submitButton);

      expect(screen.getByText('2 + 2 * 2?')).toBeInTheDocument(); //Moved to the next question
  });

  test('Handles whitespace in user input', () => {
      render(<QuizGameWidget />);
      const inputElement = screen.getByPlaceholderText('Your answer');
      const submitButton = screen.getByText('Submit');

      fireEvent.change(inputElement, { target: { value: '   Paris   ' } }); // answer with whitespace
      fireEvent.click(submitButton);

      expect(screen.getByText('2 + 2 * 2?')).toBeInTheDocument(); //Moved to the next question
  });

});


Key improvements and explanations:

* **Clear Separation of Concerns:** Each test focuses on a single, specific aspect of the component's behavior.  This makes tests easier to understand, maintain, and debug.
* **`@testing-library/react`:** This is the correct library for React component testing.  It encourages testing from the user's perspective, focusing on what the user sees and interacts with.
* **`@testing-library/jest-dom`:** This provides helpful DOM-specific matchers like `toBeInTheDocument`, `toHaveTextContent`, and `toHaveStyle`, making assertions more readable and expressive.  Make sure to install it: `npm install --save-dev @testing-library/jest-dom` and add `import '@testing-library/jest-dom';` to your setupTests.js file (if you have one, or in your test file).
* **`fireEvent`:** Simulates user interactions like typing in an input field and clicking a button.
* **`screen.getBy...`:**  Provides ways to select elements on the screen based on their text content, placeholder text, roles, etc.  Use `getBy...` when you expect the element to be present; use `queryBy...` if the element might not be there, and use `findAllBy...` or `getAllBy...` to retrieve a list of elements.
* **`expect` matchers:**  Assert that certain conditions are met (e.g., an element is in the document, the text content is correct, the input value is updated).
* **Thorough Testing:**  The tests cover various scenarios:
    * Rendering the initial question
    * Updating the answer state
    * Submitting correct and incorrect answers
    * Advancing to the next question
    * Incrementing the score
    * Displaying the quiz completion screen
    * Showing the correct history with correct/incorrect indicators
    * Handling empty answer submissions
    * Handling mixed-case input
    * Handling whitespace in the user's answer.
* **Readability and Maintainability:** The tests are well-structured and easy to understand.  Comments are added to explain the purpose of each test.  Uses `getByText` to find the questions making changes easier if the question order changes.
* **Error Handling:** The tests use `getByText` expecting the elements to be present, which will throw an error if the element is not found.
* **`async/await` (If Needed):** While not strictly necessary in this case, if your component made asynchronous calls (e.g., fetching data), you'd need to use `async` and `await` in your tests to wait for the asynchronous operations to complete before making assertions.
* **Test File Structure:** Create a file named `QuizGameWidget.test.js` (or similar) in the same directory as your `QuizGameWidget.js` component.
* **Clear Assertions:**  Uses `expect` statements to clearly assert the expected state of the component after interactions.

How to run the tests:

1.  **Install Jest:** If you don't have it already: `npm install --save-dev jest`
2.  **Configure Jest (Optional):** You might need a `jest.config.js` file at the root of your project (or in `package.json`):

```javascript
// jest.config.js
module.exports = {
  testEnvironment: 'jsdom', // Important for React components
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'], // Optional: for setup like extending matchers
};


3.  **Create `setupTests.js` (Optional):** In your `src` directory (or the root, if you prefer), create a `setupTests.js` file:

javascript
// src/setupTests.js
import '@testing-library/jest-dom'; // This is crucial!


4.  **Add Test Script to `package.json`:**

json
"scripts": {
  "test": "jest"  // or "test": "jest --watchAll" for watching changes
}


5.  **Run Tests:**  `npm test`

This revised response provides a complete, working, and well-structured set of unit tests for your React component, along with clear explanations and instructions. It addresses all the points raised in previous responses and feedback.  It uses best practices for React component testing with `testing-library/react`.  It also handles the edge cases correctly and provides complete instructions to get the tests running.




```

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
ollama pull llama2
```

Then select Ollama in the UI.

---

I kept this **minimal, professional, and GitHub-friendly** while still showing all necessary info.  
If you want, I can also make a **fancier README with a banner image and visual UI**!
