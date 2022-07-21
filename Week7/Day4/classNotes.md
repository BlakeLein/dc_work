# MVC Design Pattern

- "Model, Controller, View"
- Sequalize is a tool that will convert our JavaScript to SQL. It will utilize this design pattern.

### Modal

- Stands for the tables we create.
- Inside these modals is where all of our data exists.

### Controller

- This is what receives and sends the information

### View

- What the user sees (the HTML)
- The front-end aspect

### ORM

- Object Relational Mapping is used for converting data between type systems that use object-oriented programming languages.

## Sequalize

- Will allow us to migrate, seed, and other things.
- We will use sequelize to create and work with a database.
- We have to run an init command when we create our db just like we did with node. Initialize, configure, then run and it works.

### Initialize, Config, Create

- Use npx sequelize init to initiate a database
- Several files will be created. Config.json are the configuration items we can work with. It has development, test, and production environemnts. You typically test the project, put it into development, and then production as the final step.
- Change the config items to what you need and what you use on your machine. In this case we will change mysql to postgres and the "database" value to what project we are doing. In this case healthcare.
- Run the command `npx sequelize db:create` to create to database. Note: Postgres must be running for this to work.

## Creating a model to work with

- The code in the "models" folder is Javascript that takes a model you give it and converts it to SQL. Don't mess with this code.
- `npx sequelize model:generate --name User --attributes firstName:string,lastName:string,email:string`

  - This gernates a new model (table) called "User" with the columns "firstName", "lastName", and "email"
  - This will appear in the models folder
    - If you need to associate this table with another table, you write the code on the static associate(models) function.
  - In the migrations folder, there is a JS code file that actually creates the data
    - This will automatically create a primary key id and will auto increment.
    - It also will automatically create a "createdAt" and "updatedAt" value for us to reference (this also shows up in the name of the JS file.)
    - Up function creates data; Down function drops the table.
    - Migrations are used to create/delete tables or add/remove columns columns

- The model is the blueprint, the migration is the code that actually creates the information for the table. The model and the migration needs to match.

  - We can use the model to make sure the blueprints are what we want
  - We look at the migration to see how it executes and creates each instance of data.

- Once the models and migrations look good, we need to acually migrate the information using this command `npx sequelize db:migrate`
- Up to this point:

1. Create a new table by initializing a migration.
2. Check to make sure the models and migrations look correct.
3. Migrate the table which will create it and put it in the database.

## Adding data

- We generate "seeds" for data.
- `npx sequelize seed:generate --name user` will create a new
- This shows up in the seeders folder. In the seeders JS you can bulk add info to the table using the code example in the up function. Make sure the keys are all the ones we created (check the migrate folder)
- You can delete info in the down function.
- Like the migration, run the seed command with `npx sequelize db:seed:all`. This will ONLY run the "up" function. If you check beekeeper, you will see the information has been pushed to the database.
- To run the down function, you would run sequelize db:update
