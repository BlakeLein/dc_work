const express = require("express");
const app = express();
// This allows you to import the models in the database
const { User } = require("../database/models");
// This allows you to utilize encrypting commands
const bcrypt = require("bcrypt");
const PORT = 3000;

// MiddleWare
// Allows us to read the req.body. Without this you can't access your body.
app.use(express.json());

// Request object we filled in postman
// {
//     "username": "joeissmart",
//     "password":"notreally"
// }

// Access the password with req.body.password. We will encrpyt it by hashing it

app.post("/create_user", async (req, res) => {
  // Access the password in our body. This format is using destructuring.
  const { username, password } = req.body;

  // When you run async stuff you can test it in a try catch
  try {
    // Gen salt is a function a part of the bcrypt object that can be passed a number of rounds of salt.
    // The higher the number the more complex the number. The computer needs to run through the number more times to make it truly complex. That's what the salt number is.
    const salt = await bcrypt.genSalt(5);
    // This function will create the hashed password. Note the two arguments it takes.
    const hashedPassword = await bcrypt.hash(password, salt);
    // Creates an encrypted user to put in the table
    const encryptedUser = {
      userName: username,
      password: hashedPassword,
      createdAt: new Date(),
      updatedAt: new Date(),
    };
    // Passes our user information into the table user
    const createUser = await User.create(encryptedUser);
    console.log(createUser);
  } catch (error) {}

  res.send("create user");
});

app.listen(PORT, console.log(`Listening on Port ${PORT}`));
