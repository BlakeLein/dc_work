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

// This line lets us use local pathing for our HTML and CSS.
// Inside our public folder we will typically put our Javascript.
// MIDDLEWARE: Let's us link static files to our html.
app.use(express.static("public"));
app.use(express.json());

//Route
app.get("/", (req, res) => {
  // Here is some js information. We can pass this in the render function. Note the syntax in the HTML document.
  const user = { name: "Blake" };
  // This will render the file "home" (from the "templates file on line 11") to the screen. render() comes from the es6 package we downloaded.
  // HTML manipulation is done and rendered on the server - much faster.
  // The HTML syntax we use works because it's through a template engine.
  res.render("home", {
    locals: {
      user: user,
      teacher: "Joe",
      students: ["Amanda", "Carlos"],
    },
  });
});

// Another route linking a separate HTML file.
app.get("/file2", (req, res) => {
  res.render("file2");
});

// This doesnt work when you go to http://localhost:3001/home because that only works on a get request.
app.post("/home", (req, res) => {
  // Send doesn't create any HTML
  res.send("Hello World!");
});

app.listen(PORT, console.log(`Listening on port ${PORT}`));
