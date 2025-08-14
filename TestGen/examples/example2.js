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
