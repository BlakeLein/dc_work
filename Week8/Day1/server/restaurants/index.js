const express = require("express");
const app = express();
const { Restaurants } = require("../../database/models");
const router = express.Router();
const bcrypt = require("bcrypt");

// Middle Ware
app.use(express.json());

// Full CRUD
// Create 1 or more restaurants
router.post("/create_restaurant", async (req, res) => {
  const { name, address, reviewScore } = req.body;

  try {
    const createRestaurant = await Restaurants.bulkCreate(req.body);
    res.send(createRestaurant);
  } catch (error) {
    res.send(error);
  }
});

// Read 1 or more restaurant by id
router.get("/by_id/:id", async (req, res) => {
  const { id } = req.params;
  const restaurantToGet = await Restaurants.findAll({
    where: {
      id: id,
    },
  });
  res.send(usersToGet);
});

// Read 1 or more restaurant by name
router.get("/by_name", async (req, res) => {
  const { name } = req.body;
  const restaurantToGet = await Restaurants.findAll({
    where: {
      name: name,
    },
  });
  res.send(restaurantToGet);
});

// Read 1 or more restaurant by address
router.get("/by_address", async (req, res) => {
  const { address } = req.body;
  const restaurantToGet = await Restaurants.findAll({
    where: {
      address: address,
    },
  });
  res.send(restaurantToGet);
});

// Update name of restaurant
// router.update();

// Update the address of the restaurant

// Delete 1 restaurant by id
// Delete 1 restaurant by name

module.exports = router;
