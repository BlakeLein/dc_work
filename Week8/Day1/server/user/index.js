const express = require("express");
const app = express();
const { User } = require("../../database/models");
const router = express.Router();
const bcrypt = require("bcrypt");

app.use(express.json());

router.get("/all_users", async (req, res) => {
  const usersToGet = await User.findAll();
  res.send(usersToGet);
});

router.get("/by_id/:id", async (req, res) => {
  const { id } = req.params;
  const usersToGet = await User.findAll({
    where: {
      id: id,
    },
  });
  res.send(usersToGet);
});

router.post("/create_user", async (req, res) => {
  const { username, password } = req.body;

  try {
    const salt = await bcrypt.genSalt(5);
    const hashedPassword = await bcrypt.hash(password, salt);
    const encryptedUser = {
      userName: username,
      password: hashedPassword,
      createdAt: new Date(),
      updatedAt: new Date(),
    };
    const createUser = await User.create(encryptedUser);
    res.send(createUse);
  } catch (error) {
    res.send(error);
  }
});

router.post("/login", async (req, res) => {
  const { username, password } = req.body;
  try {
    const findUser = await User.findOne({
      where: {
        userName: username,
      },
    });
    const userWeFound = findUser.dataValues;

    const validated = await bcrypt.compare(password, userWeFound.password);
    console.log(validated);

    if (!findUser) {
      res

        .status(400)
        .send(
          "That user does not exist in our database. Did you get the username correct?"
        );
    } else {
      res.status(200).send(findUser.dataValues);
    }
  } catch (error) {
    res.send("didnt find ya");
  }
});

module.exports = router;
