// ENV import. ALWAYS at the very top of a file.
require("dotenv").config();

// Import Express
const express = require("express");

// Import supabase info
const { createClient } = require("@supabase/supabase-js");
// Initialize supabase database location (Joe's)
const supabase = createClient(process.env.SUPABASE_URL, process.env.JOE_KEY);
// Define app
const app = express();
// If there is no port defined in the env file it defaults to 3000.
const PORT = process.env.PORT || 3000;

// This allows our server to read json
app.use(express.json());

app.post("/create_student", async (req, res) => {
  console.log(req.body);
  const { data, error } = await supabase.from("web-06-22").insert([req.body]);
  if (data) {
    res.send(data);
  }
  res.send(error);
});

app.listen(PORT, console.log(`Listening on port ${PORT}`));
