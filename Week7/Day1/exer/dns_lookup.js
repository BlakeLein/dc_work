// Import dns and readline
const dns = require("dns");
// createInterface
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

// readline.question gives a prompt
// Takes 2 arguments -- 1. Prompt string, 2. Function with the url parameter.
readline.question("Domain Name: ", function (url) {
  // No idea what this does
  readline.close();
  // DNS has a look up function
  // Takes 2 arguments == 1. url to look up, 2. function with error and address parameters.
  dns.lookup(url, function (error, address) {
    // If error == true:
    if (error) {
      console.log(error.message);
      return;
    }
    // else log the IP Address we found.
    console.log("IP Address: ", address);
  });
});
