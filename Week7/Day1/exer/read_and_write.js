// Initialize our modules
const fs = require("fs");
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Ask for the input file - result becomes inputFile parameter
readline.question("Input file: ", function (inputFile) {
  // Read the first file and check for error.
  fs.readFile(inputFile, function (error, buffer) {
    if (error) {
      console.log(error.message);
      readline.close();
      return;
    }
    // Ask for output file name - result becomes outputFile parameter
    readline.question("Output file: ", function (outputFile) {
      readline.close();
      // Take content from input file, make it a string, and uppercase it.
      const content = buffer.toString();
      const upperCased = content.toUpperCase();
      // Write file function that takes the output file name, the uppercased text from the input file.
      fs.writeFile(outputFile, upperCased, function (error) {
        // Check again for an error.
        if (error) {
          console.log(error.message);
          return;
        }
        // Tell us it logged if the filename was a success.
        console.log("Wrote to file ", outputFile);
      });
    });
  });
});
