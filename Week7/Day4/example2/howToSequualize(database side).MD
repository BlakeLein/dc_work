# Making a New DataBase with Sequelize

1. Download Packages
   `npm i sequelize sequelize-cli pg express`
2. Set up Server
   - Separate folder with server
   - Import express, define app as express(), define a port#, activate port with app.listen()
3. Set up sequelize

   - Initialize your folder for your sequelize database. We run the command `npx sequelize init`.
   - This creates a `config.js` file that you will have to edit and figure out what the user/passwrods for the local postgres installed on your computer(localhost only) or put in credentials for whatever online database you are using.
   - Put the sequelize folders into one folder called "sequelize"

4. Start the database.

   - Run `npx sequelize db:create` to create the database based on the credentials and config you made in the `config.js`

5. Create models - Models become the tables and they are the way we can interact with our database tables. They provide a JS object that we can then import into our server. - `npx sequelize model:generate --name NameOfTable --attributes nameOfColumns` - Ex: `npx sequelize model:generate --name Clients --attributes firstName:string,lastName:string,email:string,pet:string `

6. Run a migration to put the model in our database.

   - Check the model and migrations to make sure it's what you want. Any changes in the model should be done in the migration as well BEFORE the migration takes place.
   - Migrations will run for all of the migrations we have (created tables)
   - Use `npx sequelize db:migrate`
   - You can now confirm this information in your database

7. (Optional) Seed Data
   - You want to seed in data that makes sense for your database when you test it.
   - Command is `npx sequelize seed:generate --name Clients`
     - This creates a seed file name clients. Inside of this file you can add data based on the commented out code. You can add your code here.
     - Seed data is just data to play around with so we hard code it here.
     - Make a seed folder for every model you have
   - Once you have the seed fules created, you can go ahead and run the seed command to populate your database with that information.
   - `npx sequelize db:seed:all`
