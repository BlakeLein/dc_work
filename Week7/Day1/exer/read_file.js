// Initialize our modules
const fs = require("fs");
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Uses readline's question function to take input. Input value is saved to "file" parameter.
readline.question("Filename: ", (file) => {
  // Still not sure what this does.
  readline.close();
  // fs' readFile function takes a file (input value), and then runs another function with error and buffer.
  fs.readFile(file, (error, buffer) => {
    // In case of an error, print the designated error message.
    if (error) {
      console.log(error.message);
      return;
    }
    // Content is buffer (file's content) converted to a string
    const content = buffer.toString();
    // Uppercase the content
    const upperCased = content.toUpperCase();
    console.log(upperCased);
  });
});
