const express = require("express");
// this imports the users dictionary from the models folder.
const { User } = require("./models");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.send("Hello!");
});

// Read all users
app.get("/users", async (req, res) => {
  const users = await User.findAll();
  res.send(users);
});

// Read a user by ID
app.get("/users/:id", async (req, res) => {
  const id = req.params.id;
  console.log(id);
  const users = await User.findByPk(id);
  res.send(users);
});

// Read a user by name
app.get("/user_name/:name", async (req, res) => {
  const name = req.params.name;
  const users = await User.findOne({
    where: {
      firstName: name,
    },
  });
  res.send(users);
});

app.listen(port, () => console.log(`Listening on port ${port}`));
