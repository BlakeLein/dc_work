import "./App.css";

import { useState } from "react";

function App() {
  const defaultForm = {
    name: "",
    password: "",
    email: "",
    address: "",
  };
  const [formData, setFormData] = useState(defaultForm);

  const validateInput = (text, name) => {
    switch (name) {
      case "name":
        // Name validation greater than five characters
        setFormData({ ...formData, [name]: text });
        break;
      case "email":
        // Coded out example - this is how we would use regex to validate the input
        // Email validation - contains the @ symbol
        setFormData({ ...formData, [name]: text });
        break;
      case "password":
        // Password validation
        setFormData({ ...formData, [name]: text });
        break;
      case "address":
        // Address validation
        setFormData({ ...formData, [name]: text });
        break;
    }
  };
  return (
    <div className="App">
      <h1>Form</h1>
      <div className="form-container">
        <form>
          <input
            onChange={(e) => validateInput(e.target.value, e.target.name)}
            value={formData.name}
            name="name"
            placeholder="Name"
            type="text"
          />
          <input
            onChange={(e) =>
              // ...formData is called "spreading" so we don't override the formData contents
              validateInput(e.target.value, e.target.name)
            }
            value={formData.email}
            name="email"
            placeholder="Email"
            type="text"
          />
          <input
            onChange={(e) =>
              // ...formData is called "spreading" so we don't override the formData contents
              validateInput(e.target.value, e.target.name)
            }
            value={formData.password}
            name="password"
            placeholder="Password"
            type="text"
          />
          <input
            onChange={(e) =>
              // ...formData is called "spreading" so we don't override the formData contents
              validateInput(e.target.value, e.target.name)
            }
            value={formData.address}
            name="address"
            placeholder="Address"
            type="text"
          />
          <input type="submit" value="Submit" />
        </form>
      </div>
    </div>
  );
}

export default App;
