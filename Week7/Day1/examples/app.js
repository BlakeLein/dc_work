// Old way
// const app = require("express");

// New way (must have "type":"module" in package.json)
import express from "express";
const app = express();

// Create a port
const PORT = 3001;
app.use(express.json());

// Routes - usually has the type of request (get or post).
// Will always include in this order a request and response (you can just put req and res)
// You can put whatever code you want inside this code block. It executes when you call the route (like in postman)
console.log("I am outside the route"); // This runs immediately because it's not in the route
app.get("/", (req, res) => {
  console.log("I am inside the route"); // This only runs when we call the route. Routes are asyncronous functions with a condition
  // IF it's a GET and IF it's to this address, execute this code.
  res.send("this is the home page");
});

// We put benji here so this route would have a different name than the last route. If two routes have the same name the last one will always run.
app.get("/benji", (req, res) => {
  req.send("Lizard");
});

// We would need to use post instead of get
app.post("/beer", (req, res) => {
  req.send("Beer");
});

// This is how you would create a form that took in data from the front end and send it to the back end.
app.post("/create_user", (req, res) => {
  res.send(`I have created user ${req.body.discplayer}`);
});

import * as cowsay from "cowsay";

app.get("/cow1", (req, res) => {
  res.send(
    cowsay.say({
      text: "I'm a moooodule",
      e: "oO",
      T: "U ",
    })
  );
});

app.post("/cow2", (req, res) => {
  res.send(
    cowsay.say({
      text: req.body.text,
      e: "oO",
      T: "U ",
    })
  );
});

app.post("/cow3", (req, res) => {
  res.send(
    cowsay.say({
      text: req.body.text1,
      e: "xx",
      T: "Blake ",
    })
  );
});

// Puts the server online at that port number
app.listen(PORT, console.log(`Listening on port ${PORT}`));
