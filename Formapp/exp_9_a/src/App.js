import { useState } from "react";

export default function App() {
  const [formData, setFormData] = useState ({
    name: "",
    rollno: ""
  });

  const handleChange = (e) => {
    const {name,value} = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [ name ]: value
    }));
    };

    const handleSubmit = (e) => {
      e.preventDefault();
      console.log("Form Submitted: ", formData);
      alert(`Name: ${formData.name}\nRoll No: ${formData.rollno}`);
    };
    return (
      <div>
       <form onSubmit={handleSubmit}>
       <h2>React Form</h2>
      <div>
        <label>Name: </label>
        <input type="text" name="name" value={formData.name}
          onChange={handleChange}required/>
      </div>
      <div>
        <label>Roll No: </label>
        <input type="text" name="rollno" value={formData.rollno}
          onChange={handleChange}required/>
      </div>
      <button type = "submit">Submit</button>
      </form>
      </div>
    );
  }