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

As an example Gemini-2.0-flash has been considered 

In order to test we have taken the below JavaScript Code 

source to the example code can be downloaded from [here](https://github.com/PrateekJanagouda/Frontend-AI-Tooling-Challenge/blob/main/TestGen/examples/example1.js)


---

## 1 . Gemini with Google studio's Free API key and the Raw output for this is 


Raw output of the example code can be found [here](https://github.com/PrateekJanagouda/Frontend-AI-Tooling-Challenge/blob/main/TestGen/examples/example1_output.js)

---

##  Example 2

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
