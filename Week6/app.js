const express = require("express");
const app = express();
const PORT = 3001;

console.log("Howdy");
app.listen(PORT, console.log(`Server is running on port ${PORT}`));
