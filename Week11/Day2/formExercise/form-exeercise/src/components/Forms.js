import React from "react";
import { useState } from "react";
import "../App.css";

export default function Forms() {
  const defaultForm = {
    first: "",
    last: "",
    email: "",
    password: "",
  };

  const [formData, setFormData] = useState(defaultForm);

  const validateInput = (text, name) => {
    switch (name) {
      case "first":
        // Name validation greater than five characters
        setFormData({ ...formData, [name]: text });
        break;
      case "last":
        // Coded out example - this is how we would use regex to validate the input
        // Email validation - contains the @ symbol
        let regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        if (regex.test(text)) {
          setFormData({ ...formData, [name]: text });
          break;
        }
        alert("Please enter a valid email format.");
      case "email":
        // Password validation
        setFormData({ ...formData, [name]: text });
        break;
      case "password":
        // Address validation
        setFormData({ ...formData, [name]: text });
        break;
    }
  };

  return (
    <div className="form-side">
      <div className="form">
        <div className="buttons">
          <button>Connect with Facebook</button>
          <button>Connect with Twitter</button>
        </div>
        <p>or sign up with</p>
        <div className="names">
          <input
            onChange={(e) => validateInput(e.target.value, e.target.name)}
            value={formData.first}
            name="first"
            placeholder="First Name"
            type="text"
          />
          <input
            onChange={(e) => validateInput(e.target.value, e.target.name)}
            value={formData.last}
            name="last"
            placeholder="Last Name"
            type="text"
          />
        </div>
        <input
          onChange={(e) => validateInput(e.target.value, e.target.name)}
          value={formData.email}
          name="email"
          placeholder="Email Address"
          type="text"
        />
        <input
          onChange={(e) => validateInput(e.target.value, e.target.name)}
          value={formData.password}
          name="password"
          placeholder="Password"
          type="text"
        />
        <p>
          By creating an account, you agree to our{" "}
          <a href="">Terms & Conditions</a>
        </p>
        <input type="submit" value="Create Account" />
        <p>
          Template by <a href="">w3Layouts</a>
        </p>
      </div>
    </div>
  );
}
