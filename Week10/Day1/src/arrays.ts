let students: string[] = ["Amanda", "Carlos", "Rahmin", "West"];

//Any isn't the best thing to use because it defeats the purpose of typescript
let get: any[] = ["Amanda", 14, true];
let ages: number[] = [1, 9, 14];
// This works
ages.push(12);

// This is not the best way to structure an object in typescript
let user: object = {
  name: "Joe",
};

// Type Alias - Use pascal casing. Declare the object structure here and simply call it later.
type User = {
  name: string;
  age: number;
  readonly emailAddress: string; // Readonly means you can't reassign the variable
  optional?: string; // This is now an optional string because of the ?
};

let amanda: User = {
  name: "Amanda",
  age: 24,
  emailAddress: "amandah@gmail.com",
};

// Syntax for array of objects
const listOfUsers: User[] = [];
listOfUsers.push(amanda);

type Password = {
  password: string | number; // This password can be a string or a number.
  securtityClearance: "Basic" | "Top Secret"; // This value can only be one of these two strings
};

type SoftwareEngineer = {
  readonly id: number;
  password: Password;
};

const blke: SoftwareEngineer = {
  id: 12201,
  password: {
    password: 7777,
    securtityClearance: "Basic",
  },
};
