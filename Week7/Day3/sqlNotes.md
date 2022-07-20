# SQL Intro (Postgres)

- Used to make and work with databases. Info is related to each other so they are relational databases.

## Using it!

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
