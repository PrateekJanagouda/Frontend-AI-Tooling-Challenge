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
