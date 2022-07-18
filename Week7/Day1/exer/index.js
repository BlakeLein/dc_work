// Import the http module
const http = require("http");

// Creates IP address host name and port #
const hostname = "127.0.0.1";
const port = 3000;

// Creates server
const server = http.createServer((req, res) => {
  //Passes the '200' status code on sucess
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  // This text displays on the browser as plain text
  res.end("This is what displays on the brower!");
});

// Starts server - Always put at the end.
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
