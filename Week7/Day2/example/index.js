// this is the "import" syntax
import express from "express";
const app = express();
const PORT = 3001;

// MIDDLEWARE: Setting up the template engine - code provided by es6's template engine documentation.
import es6Renderer from "express-es6-template-engine";
// Engine is going to render HTML using the es6Renderer tool
app.engine("html", es6Renderer);
// "templates" is a file that contains all of our html files
app.set("views", "templates");
//
app.set("view engine", "html");

//Route
app.get("/", (req, res) => {
  //   res.send("Hello World!");
  // This will render the file "home" (from the "templates file on line 11") to the screen. render() comes from the es6 package we downloaded.
  res.render("home");
});

// Another route linking a separate HTML file.
app.get("/file2", (req, res) => {
  res.render("file2");
});

// This doesnt work when you go to http://localhost:3001/home because that only works on a get request.
app.post("/home", (req, res) => {
  res.send("Hello World!");
});

app.listen(PORT, console.log(`Listening on port ${PORT}`));
