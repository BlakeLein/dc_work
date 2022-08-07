const express = require("express");
const app = express();
// This allows you to import the models in the database
const { User } = require("../database/models");
// This allows you to utilize encrypting commands

const user = require("../database/models/user");
const PORT = 3000;
const router = express.Router();
const es6Renderer = require("express-es6-template-engine");

const userRoutes = require("./user");
const restaurantRoutes = require("./restaurants");

// MiddleWare
// Allows us to read the req.body. Without this you can't access your body.
app.use(express.json());

// Template Engine
app.use(express.static("public"));
app.engine("html", es6Renderer);
app.set("views", "../public/views");
app.set("view engine", "html");

app.use("/users", userRoutes);
app.use("/restaurants", restaurantRoutes);

app.get("/", (req, res) => {
  res.render("index");
});

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
    res.send(createUser);
  } catch (error) {
    res.send(error);
  }

  res.send("create user");
});

// Decrypting on Login
app.post("/login", async (req, res) => {
  const { username, password } = req.body;
  try {
    // Find the user based on a username
    const findUser = await User.findOne({
      where: {
        userName: username,
      },
    });
    const userWeFound = findUser.dataValues;
    // The hashed password is userWeFound.password

    // Checks to see if the password entered matches the encrypted password. Returns a boolean of whether or not they match
    // Decrypts and compares all in one.
    const validated = await bcrypt.compare(password, userWeFound.password);
    console.log(validated);

    // Run this code if you don't find them.
    if (!findUser) {
      res
        // If they fail the login do this.
        .status(400)
        .send(
          "That user does not exist in our database. Did you get the username correct?"
        );
    } else {
      // If they log in successfully do this.
      res.status(200).send(findUser.dataValues).redirect("/homepage");
    }
  } catch (error) {
    res.send("didnt find ya");
  }
});

// Updating a Password

app.post("/update_password", async (req, res) => {
  const { username, password, newPassword } = req.body;

  try {
    // Find the user based on a username
    const findUser = await User.findOne({
      where: {
        userName: username,
      },
    });

    // Run this code if you don't find them.
    if (!findUser) {
      res
        // If they fail the login do this.
        .status(400)
        .send(
          "That user does not exist in our database. Did you get the username correct?"
        );
    } else {
      // If they log in successfully do this.
      const userWeFound = findUser.dataValues;
      // Decrypts and compares all in one.
      const validated = await bcrypt.compare(password, userWeFound.password);
      if (validated == true) {
        userWeFound.update({
          password: newPassword,
        });
      }
      console.log(userWeFound.password);
    }
  } catch (error) {
    res.send("didnt find ya");
  }
});

app.listen(PORT, console.log(`Listening on Port ${PORT}`));
