# SQL Intro (Postgres)

- Used to make and work with databases. Info is related to each other so they are relational databases.

## Creating a table

- CREATE TABLE Person (
  PersonId SERIAL PRIMARY KEY,
  Name TEXT NOT NULL
  );

- Creates a table called "Person"
- Rows in a table need to be unique. The data doesn't have to be unique, but each row needs a "unique ID". The same piece of data on different rows will have a different ID.
- The "primary key" of the table is the absolute unique identifier of a table. Like a single person having an individualized social security number. You want primary keys to automatically generate.
  - You can use the SERIAL command that will automatically number rows from the command serial.
  - The primary key is typically the PersonId
  - MUST INCLUDE COMMAS BETWEEN ROW NAMES
- This table has two rows - PersonId and Name.
- The TEXT NOT NULL makes this a required field. Anything not required doesn't need the NOT NULL
- You can press \dt to view all tables in the database.
- This table is connected to the database we were inside of with the terminal.
- Postgres is a "flavor" of SQL
- \d (table name) will show the table by name

## Add to a table

INSERT INTO Person (NAME) VALUES ('Blake');

- This returns "Insert 0 1" which usually means it was a success.
- this command inserts the value "Blake" into the name row of the table called "Person"

## Beekeeper studio

- A program that makes the SQL look nice
- Open and select postgres. Now that postgres is installed we can run all our SQL through here instead.
- id has a blue key - that's how you know it's a primary key for the row.

## How it works

- Client connects to a server which connects to a database. The connection is the tricky part.

## How to Select from a table

- SELECT \* FROM CARTOONS will select all info in the cartoons table.
- SELECT \* FROM CARTOONS WHERE id = 1 will select any item from the entire table where id is equal to
- There are several commands for selecting/reading info from a database.

## Updating Existing Information

- UPDATE Cartoons SET year_created = '1986' WHERE cartoon_show = 'Courage the Cowardly Dog';
  - This changes the year to 1986 for all items that have "Courage the Cowardly Dog" in the cartoon_show column.
  - If you only wanted to update one item, you would update by ID not by data value.

## Destroying Data

- We don't delete "some" information from the row - typically we delete the entire row.
- DELETE FROM cartoons WHERE cartoon_show = 'Courage the Cowardly Dog'; will delete any item in a table that has the cartoon_show value 'Courage the Cowardly Dog'
- DROP TABLE cartoons; will completely and permanently delete a table.

## C.R.U.D.

- Stands for Create, Read, Update, Destroy. These are backend functions.
- Create- We did this when creating our table.
- Read- We did this when selecting our content.
- Update- We did this when changing the year to 1986.
- Destroy- We did this when deleting items above.
