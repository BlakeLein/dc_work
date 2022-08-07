const express = require("express");
const session = require("express-session");
const cookieParser = require("cookie-parser");
app = express();
const cors = require("cors");
PORT = 3000;
const es6Renderer = require("express-es6-template-engine");
const { User } = require("../sequelize/models");
// Imports all models
const models = require("../sequelize/models");

// Storing sessions
const SequelizeStore = require("connect-session-sequelize")(session.Store);
const store = new SequelizeStore({
  db: models.sequelize,
});

// Middle Ware
app.use(cookieParser());
app.use(
  session({
    // Store this in the env file
    secret: "secret",
    // We want the cookie to expire
    resave: false,
    saveUninitialized: true,
    store: store,
    // We don't need cookies if we are storing the session.
    // cookie: {
    //   maxAge: 2592000000,
    //   // Only make true if you have an https url
    //   secure: false,
    // },
  })
);

const cusername = "BlakeLein";
const cpassword = "Aligator7";

app.get("/", (req, res) => {
  console.log("Hi");
  res.send("Hi");
});

app.post("/login", async (req, res) => {
  console.log("Hi");
  const user = await User.findOne({
    where: {
      username: cusername,
      password: cpassword,
    },
  });
  res.send(user);
});

// Server Live
app.listen(PORT, console.log(`Listening on Port ${PORT}`));
