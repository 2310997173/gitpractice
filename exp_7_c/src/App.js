import React, { useState } from "react";

function App() {
  const [items, setItems] = useState(["HTML", "CSS", "JavaScript", "React.js"]);
  const [newItem, setNewItem] = useState("");
  const addItem = () => {
    if (newItem.trim() === "") {
      alert("Enter Valid Item!");
      return;
    }
    setItems([...items, newItem]);
    setNewItem("");
  };
  return (
    <div style={{ padding: "20px", fontFamily: "Verdana, Courier" }}>
      <h1>Single Page React App</h1>
      <p>This is a simple single-page application built with React.js.</p>
      <h2>Front-End Development</h2>
      <ul style={{ listStyleType: "circle" }}>
        {items.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>

      <h3>Add New Topic</h3>
      <input
        type="text"
        value={newItem}
        onChange={(e) => setNewItem(e.target.value)}
        placeholder="Enter a new topic"
        style={{
          padding: "8px",
          marginRight: "10px",
          borderRadius: "4px",
          border: "1px solid green",
        }}
      />
      <button
        onClick={addItem}
        style={{
          padding: "8px 16px",
          backgroundColor: "lightgreen",
          color: "blue",
          border: "none",
          borderRadius: "4px",
          cursor: "pointer",
        }}
      >
        Add Topic
      </button>
    </div>
  );
}

export default App;
