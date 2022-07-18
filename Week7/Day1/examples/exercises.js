const express = require("express");
const app = express();
const PORT = 3000;

const dns = require("dns");
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question("Domain Name: ", function (url) {
  readline.close();
  dns.lookup(url, function (error, address) {
    if (error) {
      console.log(error.message);
      return;
    }
    console.log("IP Address: ", address);
  });
});

app.listen(PORT, console.log(`Listening on port ${PORT}`));
