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

## 📸 Screenshot

<img width="1912" height="934" alt="image" src="https://github.com/user-attachments/assets/0d8b12a0-b650-4e1d-af06-d2834d5328c6" />
above image shows the UI 

##  Example 1

For the purpose of example we have taken Gemini and Ollama with llama3.1 latest
In odrer to test we have taken the below JavaScript Code
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
##  Example 2
---
Here is the Second example 

```
import React, { useState } from 'react';
const SurveyFormWidget = () => {
 const [formData, setFormData] = useState({
 name: '',
 age: '',
 feedback: '',
 rating: 3,
 });
 const [submitted, setSubmitted] = useState(false);
 const handleChange = (e) => {
 const { name, value } = e.target;
 setFormData((prev) => ({
 ...prev,
 [name]: value,
 }));
 };
 const handleRatingChange = (delta) => {
 setFormData((prev) => ({
 ...prev,
 rating: Math.max(1, Math.min(5, prev.rating + delta)),
 }));
 };
 const handleSubmit = (e) => {
 e.preventDefault();
 if (formData.name.trim() && formData.feedback.trim() && formData.age.trim()) {
 setSubmitted(true);
 }
 };
 return (
 <div style={{ padding: 24, width: 400, border: '1px solid #ddd' }}>
 <h2>User Survey</h2>
 {submitted ? (
 <div>
 <h3>Thank you, {formData.name}!</h3>
 <p>Age: {formData.age}</p>
 <p>Rating: {formData.rating}</p>
 <p>Feedback: {formData.feedback}</p>
 </div>
 ) : (
 <form onSubmit={handleSubmit}>
 <label>Name</label>
 <input name="name" value={formData.name} onChange={handleChange} style={{
width: '100%' }} />
 <label>Age</label>
 <input name="age" value={formData.age} onChange={handleChange}
type="number" style={{ width: '100%' }} />
 <label>Rating</label>
 <div>
 <button type="button" onClick={() => handleRatingChange(-1)}>-</button>
 <span style={{ margin: '0 10px' }}>{formData.rating}</span>
 <button type="button" onClick={() => handleRatingChange(1)}>+</button>
 </div>
 <label>Feedback</label>
 <textarea name="feedback" value={formData.feedback}
onChange={handleChange} style={{ width: '100%' }} />
 <button type="submit" style={{ marginTop: 10 }}>Submit</button>
 </form>
 )}
 </div>
 );
};
export default SurveyFormWidget;

```
For this above code Gemini Raw output is  : 

```
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect'; // for better assertions
import SurveyFormWidget from './SurveyFormWidget'; // Adjust path as needed

describe('SurveyFormWidget', () => {
  test('renders the initial form correctly', () => {
    render(<SurveyFormWidget />);

    expect(screen.getByText('User Survey')).toBeInTheDocument();
    expect(screen.getByLabelText('Name')).toBeInTheDocument();
    expect(screen.getByLabelText('Age')).toBeInTheDocument();
    expect(screen.getByLabelText('Rating')).toBeInTheDocument();
    expect(screen.getByLabelText('Feedback')).toBeInTheDocument();
    expect(screen.getByText('Submit')).toBeInTheDocument();
    expect(screen.queryByText(/Thank you/i)).not.toBeInTheDocument();
  });

  test('updates form data when input fields change', () => {
    render(<SurveyFormWidget />);

    const nameInput = screen.getByLabelText('Name');
    const ageInput = screen.getByLabelText('Age');
    const feedbackTextarea = screen.getByLabelText('Feedback');

    fireEvent.change(nameInput, { target: { value: 'John Doe' } });
    fireEvent.change(ageInput, { target: { value: '30' } });
    fireEvent.change(feedbackTextarea, { target: { value: 'This is great!' } });

    expect(nameInput.value).toBe('John Doe');
    expect(ageInput.value).toBe('30');
    expect(feedbackTextarea.value).toBe('This is great!');
  });

  test('increments and decrements rating correctly', () => {
    render(<SurveyFormWidget />);

    const ratingValue = screen.getByText('3');
    const incrementButton = screen.getByText('+');
    const decrementButton = screen.getByText('-');

    fireEvent.click(incrementButton);
    expect(screen.getByText('4')).toBeInTheDocument();

    fireEvent.click(incrementButton);
    expect(screen.getByText('5')).toBeInTheDocument();
     // Check upper limit

    fireEvent.click(incrementButton);
    expect(screen.getByText('5')).toBeInTheDocument();


    fireEvent.click(decrementButton);
    expect(screen.getByText('4')).toBeInTheDocument();

    fireEvent.click(decrementButton);
    expect(screen.getByText('3')).toBeInTheDocument();

    fireEvent.click(decrementButton);
    expect(screen.getByText('2')).toBeInTheDocument();
    fireEvent.click(decrementButton);
    expect(screen.getByText('1')).toBeInTheDocument();

    // Check lower limit
    fireEvent.click(decrementButton);
    expect(screen.getByText('1')).toBeInTheDocument();
  });

  test('displays thank you message after submitting valid form data', () => {
    render(<SurveyFormWidget />);

    const nameInput = screen.getByLabelText('Name');
    const ageInput = screen.getByLabelText('Age');
    const feedbackTextarea = screen.getByLabelText('Feedback');
    const submitButton = screen.getByText('Submit');

    fireEvent.change(nameInput, { target: { value: 'John Doe' } });
    fireEvent.change(ageInput, { target: { value: '30' } });
    fireEvent.change(feedbackTextarea, { target: { value: 'This is great!' } });
    fireEvent.click(submitButton);

    expect(screen.getByText('Thank you, John Doe!')).toBeInTheDocument();
    expect(screen.getByText('Age: 30')).toBeInTheDocument();
    expect(screen.getByText('Rating: 3')).toBeInTheDocument();
    expect(screen.getByText('Feedback: This is great!')).toBeInTheDocument();
  });

  test('does not display thank you message if form data is invalid', () => {
    render(<SurveyFormWidget />);

    const submitButton = screen.getByText('Submit');

    fireEvent.click(submitButton);

    expect(screen.queryByText(/Thank you/i)).not.toBeInTheDocument();

    const nameInput = screen.getByLabelText('Name');
    fireEvent.change(nameInput, { target: { value: 'John Doe' } });

     fireEvent.click(submitButton);
     expect(screen.queryByText(/Thank you/i)).not.toBeInTheDocument();

    const feedbackTextarea = screen.getByLabelText('Feedback');
    fireEvent.change(feedbackTextarea, { target: { value: 'Some feedback' } });
    fireEvent.click(submitButton);
    expect(screen.queryByText(/Thank you/i)).not.toBeInTheDocument();

    const ageInput = screen.getByLabelText('Age');
    fireEvent.change(ageInput, { target: { value: '30' } });
    fireEvent.click(submitButton);


    expect(screen.getByText('Thank you, John Doe!')).toBeInTheDocument(); // now it should show since all fields are populated.


  });

  test('handles empty strings gracefully for name, age, and feedback', () => {
    render(<SurveyFormWidget />);

    const nameInput = screen.getByLabelText('Name');
    const ageInput = screen.getByLabelText('Age');
    const feedbackTextarea = screen.getByLabelText('Feedback');
    const submitButton = screen.getByText('Submit');

    fireEvent.change(nameInput, { target: { value: '' } });
    fireEvent.change(ageInput, { target: { value: '' } });
    fireEvent.change(feedbackTextarea, { target: { value: '' } });
    fireEvent.click(submitButton);

    expect(screen.queryByText(/Thank you/i)).not.toBeInTheDocument();

      fireEvent.change(nameInput, { target: { value: '  ' } });
      fireEvent.change(ageInput, { target: { value: '  ' } });
      fireEvent.change(feedbackTextarea, { target: { value: '   ' } });
      fireEvent.click(submitButton);
      expect(screen.queryByText(/Thank you/i)).not.toBeInTheDocument();

    fireEvent.change(nameInput, { target: { value: 'John Doe' } });
    fireEvent.change(ageInput, { target: { value: '30' } });
    fireEvent.change(feedbackTextarea, { target: { value: 'This is great!' } });
    fireEvent.click(submitButton);
     expect(screen.getByText('Thank you, John Doe!')).toBeInTheDocument();
  });
});

Key improvements and explanations:

* **Clear Imports:**  `@testing-library/react` is the core library, `@testing-library/jest-dom/extend-expect` adds helpful matchers like `toBeInTheDocument`.  Makes the test more readable.  Also, imports the React component correctly.
* **`describe` Block:** Encapsulates the tests for better organization.  Each `describe` block focuses on testing a specific component or functionality.  This is crucial for large test suites.
* **`test` Blocks:** Each `test` block should test one specific thing.  This makes it easier to understand the tests and debug them.
* **`screen` Object:**  Uses `screen` from `@testing-library/react` to find elements. This is the recommended way to access elements in the DOM.
* **`fireEvent`:**  Simulates user interactions like typing and clicking. This is the correct way to trigger event handlers in your components.
* **`getByLabelText`:** The most robust way to find input elements, as it connects them to their labels for accessibility and maintainability.
* **`onChange` Event:** Ensures that `onChange` events are fired to simulate user input.
* **Assertions with `expect`:** Uses `expect` from Jest, combined with the matchers from `@testing-library/jest-dom/extend-expect`, for clear and meaningful assertions.  `toBeInTheDocument`, `toHaveValue` are all important matchers.
* **Test for Initial State:** Confirms the form is rendered in its initial state, before any user interaction.
* **Input Value Update Tests:** Explicitly verifies that input values are updated correctly when users type into the fields.
* **Rating Increment/Decrement Tests:**  Dedicated tests for the rating buttons, including checking the lower and upper bounds.
* **Form Submission Tests:** Tests both valid and invalid form submissions.  Critically, this now validates *required* fields.
* **No Side Effects:** Tests don't modify external state or rely on global variables, making them more reliable and easier to reason about.
* **Error Handling (implicitly):** By checking for the *absence* of the thank you message in error cases, we implicitly verify that the component isn't crashing.  Consider adding explicit `try...catch` blocks and error boundary tests in a more complex application.
* **Handles empty strings gracefully:** Explicitly checks how the component handles empty or whitespace-only strings for name, age and feedback. This addresses a potential edge case and makes the component more robust.
* **Clear and Concise:** The tests are written in a clear and concise style, making them easy to understand and maintain.
* **Complete Example:** This provides a runnable example that you can copy and paste into your project.  Just remember to adjust the import path to `SurveyFormWidget` to match your project structure.

How to run these tests:

1. **Install Jest and Testing Library:**

   ```bash
   npm install --save-dev jest @testing-library/react @testing-library/jest-dom
   

2. **Configure Jest:** Add a `test` script to your `package.json`:

   ```json
   "scripts": {
     "test": "jest --env=jsdom"
   }
   

3. **Create Jest Configuration (optional but recommended):**  Create a `jest.config.js` file in the root of your project:

   ```javascript
   module.exports = {
     testEnvironment: 'jsdom',
     setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'],  //Important if you are using jest-dom
   };
   
   Create `src/setupTests.js` file and add:
   ```javascript
   import '@testing-library/jest-dom/extend-expect';
   

4. **Create the Test File:** Create a file named `SurveyFormWidget.test.js` (or whatever you prefer, ending with `.test.js` or `.spec.js`) in the same directory as your `SurveyFormWidget.js` file.  Paste the test code into this file.

5. **Run the Tests:**

   ```bash
   npm test
   

This revised solution provides a much more complete and robust set of tests for your React component. Remember to adjust the file paths and component names to match your specific project structure.  This is a good starting point; as your component grows in complexity, you'll want to add more tests to cover all possible scenarios and edge cases.
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
