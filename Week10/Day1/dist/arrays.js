"use strict";
let students = ["Amanda", "Carlos", "Rahmin", "West"];
//Any isn't the best thing to use because it defeats the purpose of typescript
let get = ["Amanda", 14, true];
let ages = [1, 9, 14];
// This works
ages.push(12);
// This is not the best way to structure an object in typescript
let user = {
    name: "Joe",
};
let amanda = {
    name: "Amanda",
    age: 24,
    emailAddress: "amandah@gmail.com",
};
// Syntax for array of objects
const listOfUsers = [];
listOfUsers.push(amanda);
const blke = {
    id: 12201,
    password: {
        password: 7777,
        securtityClearance: "Basic",
    },
};
