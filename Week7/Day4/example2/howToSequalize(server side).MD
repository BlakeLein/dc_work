# How to Run a server with sequelize

1. Install necessary tools for your server. That would be:

```
npx i express sequelize-cli
```

2. Set up server.

```
const express = require("express");
// this imports the users dictionary from the models folder.
const { User } = require("./models");
const app = express();
const port = 3000;

app.listen(port, () => console.log(`Listening on port ${port}`));
```

3. Import your models with require. The models that got created by sequelize have a direct connection to the tables you created in your database.
   -At the top write your code

   ```
   const { Pets, Clients } = require("../sequelize/models");
   ```

4. Build the routes you need to make CRUD work.

```
app.get("/", async (req, res) => {
  const pets = await Pets.findAll();
  res.json(pets);
});
```

- This uses the `Pets` model that was created, and runs a function on them called `findAll()`. That is a built-in function in sequelize that allows you to find all the records that are in that table.
- Here are some others to read about:
  ```
  findOne()
  findByPk()
  create()
  update()
  destroy()
  ```
- This is not a comprehensive list, so look at the sequelize docs to find more methods that we didn't include.
