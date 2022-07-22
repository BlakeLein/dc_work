const express = require("express");
const { User, Longboard, Order } = require("../database/models");
const app = express();
const PORT = 3000;

// Middleware
app.use(express.json());

// Create for user, longboard, and order
app.post("/user", async (req, res) => {
  // destructuring
  //   try {
  //     const user = await User.create({
  //       firstName: "Super",
  //       lastName: "Mario",
  //       email: "mario@plumbermail.org",
  //       password: "itsame",
  //       createdAt: new Date(),
  //       updatedAt: new Date(),
  //     });
  //     res.status(200).send(user);
  //   } catch (error) {
  //     res.status(400).send(error);
  //   }
});

app.post("/longboard", (req, res) => {
  res.send("longboard");
});

app.post("/order", (req, res) => {
  res.send("order");
});

app.listen(PORT, console.log(`Listening on Port ${PORT}`));
