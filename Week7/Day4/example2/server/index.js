const express = require("express");
const { Pets, Clients } = require("../sequelize/models");
const app = express();
const PORT = 3000;
app.use(express.json());

app.get("/pets", async (req, res) => {
  const pets = await Pets.findAll();
  res.json(pet);
});

app.get("/clients", async (req, res) => {
  const client = await Clients.findAll();
  res.json(client);
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
