const express = require("express");
app = express();
const cors = require("cors");
PORT = 3000;

const petsRoutes = require("./routes/pets");

// MiddleWare
// Allows us to read the req.body. Without this you can't access your body.
app.use(express.json());
app.use(cors());

// Template Engine
const es6Renderer = require("express-es6-template-engine");
app.use(express.static("public"));
app.engine("html", es6Renderer);
app.set("views", "./public/views");
app.set("view engine", "html");

// Routes
app.use("/pets", petsRoutes);

// Server Live
app.listen(PORT, console.log(`Listening on Port ${PORT}`));
