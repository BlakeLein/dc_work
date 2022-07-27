const express = require("express");
const app = express();
const router = express.Router();

// Middle Ware
app.use(express.json());

// Imported Models
const { PetsV2 } = require("../../../sequelize/models");
const { Owner } = require("../../../sequelize/models");

// Create
router.post("/create_pet", async (req, res) => {});

// Read
router.get("/get_pets", async (req, res) => {
  // Get the index.html page and view an html page that says "pets"
  // Connect Pets in Database
  const petInfo = await PetsV2.findAll({ raw: true });
  console.log(petInfo);

  res.render("pets", {
    //   This makes a variable available to the client.
    locals: {
      // Title is the variable containing the word 'Welcome!'
      // Take this to the HTML and do ${title}
      pets: petInfo,
    },
  });
});

router.get("/get_owners", async (req, res) => {
  const ownerInfo = await Owner.findAll({ raw: true });
  console.log(ownerInfo);
  res.render("owners", {
    locals: {
      owners: ownerInfo,
    },
  });
});

// Update
router.put("/update_pets", async (req, res) => {
  res.send("Updated that pet");
});

// Destroy
router.delete("/destroy_pets", async (req, res) => {
  res.send("Destroyed that pet");
});

// Export Anything router
module.exports = router;
