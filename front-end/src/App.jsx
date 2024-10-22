import React, { useState } from 'react';

function App() {
  // these are the different backend functions and the frontend functions to make that work
  const [form1, setForm1] = useState({ s_email: '', s_name: '', s_lang: 'English' });
  const [form2, setForm2] = useState({ e_month: '', e_day: '', e_year: '' });
  const [form3, setForm3] = useState({ student_email: '', event_date: '', event_room: '' });

  const handleSubmitForm1 = (e) => {
    e.preventDefault();
    fetch('http://localhost:5000/submit', { // the localhost:5000 is what connects it to the backend, the submit is what tells the backend what to do
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form1),
    })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((data) => console.log('Form 1 Submitted:', data))
    .catch((error) => console.error('Error:', error));
  };

  const handleSubmitForm2 = (e) => {
    e.preventDefault();
    fetch('http://localhost:5000/submit2', { // the localhost:5000 is what connects it to the backend, the submit2 is what tells the backend what to do
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form2),
    })
      .then((response) => response.json())
      .then((data) => console.log('Form 2 Submitted:', data))
      .catch((error) => console.error('Error:', error));
  };

  const handleSubmitForm3 = (e) => {
    e.preventDefault();
    fetch('http://localhost:5000/submit3', { // the localhost:5000 is what connects it to the backend, the submit3 is what tells the backend what to do
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form3),
    })
      .then((response) => response.json())
      .then((data) => console.log('Form 3 Submitted:', data))
      .catch((error) => console.error('Error:', error));
  };

  // this is all the "html" stuff like inputs and stuff
  // this can all be changed, deleted, or added, you just have to give the new things distinct names so that backend and db guys know what to do on their end
  return (
    <div>
      <form onSubmit={handleSubmitForm1}>
        <input
          type="text"
          name="s_email"
          placeholder="Enter email"
          value={form1.s_email}
          onChange={(e) => setForm1({ ...form1, s_email: e.target.value })}
          required
        />
        <input
          type="text"
          name="s_name"
          placeholder="Enter name"
          value={form1.s_name}
          onChange={(e) => setForm1({ ...form1, s_name: e.target.value })}
          required
        />
        <select
          name="s_lang"
          value={form1.s_lang}
          onChange={(e) => setForm1({ ...form1, s_lang: e.target.value })}
        >
          <option value="English">English</option>
          <option value="Spanish">Spanish</option>
          <option value="French">French</option>
        </select>
        <button type="submit">Submit</button>
      </form>

      <form onSubmit={handleSubmitForm2}>
        <input
          type="number"
          name="e_month"
          placeholder="Enter month (as number)"
          value={form2.e_month}
          onChange={(e) => setForm2({ ...form2, e_month: e.target.value })}
          min="1"
          max="12"
          required
        />
        <input
          type="number"
          name="e_day"
          placeholder="Enter day (as number)"
          value={form2.e_day}
          onChange={(e) => setForm2({ ...form2, e_day: e.target.value })}
          min="1"
          max="31"
          required
        />
        <input
          type="number"
          name="e_year"
          placeholder="Enter year"
          value={form2.e_year}
          onChange={(e) => setForm2({ ...form2, e_year: e.target.value })}
          min="2024"
          max="3000"
          required
        />
        <button type="submit">Submit</button>
      </form>

      <form onSubmit={handleSubmitForm3}>
        <input
          type="text"
          name="student_email"
          placeholder="Enter student email"
          value={form3.student_email}
          onChange={(e) => setForm3({ ...form3, student_email: e.target.value })}
          required
        />
        <input
          type="date"
          name="event_date"
          placeholder="Enter date"
          value={form3.event_date}
          onChange={(e) => setForm3({ ...form3, event_date: e.target.value })}
          required
        />
        <input
          type="text"
          name="event_room"
          placeholder="Enter room"
          value={form3.event_room}
          onChange={(e) => setForm3({ ...form3, event_room: e.target.value })}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;