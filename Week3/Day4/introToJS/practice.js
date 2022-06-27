console.log("Hello");

// This is how you make a comment

// Variables
// let, var, or const

let rahmin = "gamer";
var carlos = "meme lord";
const jason = "windows problem guy";
rahmin = "engineer";

console.log(rahmin);

// You can reassign let and var variables but not const.
// You cannot reassign const variable, but you can add elements to a list or dictionary stored in const.

//Arrays are the same as they were in python - You access them via the index
const students = ["Olivia", "Andrea", "Amanda"];
console.log(students[1]);

//Objects (dictionaries) - Syntax is a tad different
const student = {
  name: "Ethan",
  id: 3,
};

console.log(student["name"]); // Even though you don't use quotes when creating/assigning the key/value, you have to use quotes when you call them.
console.log(student.name); // Dot notation only works on objects

const restaurant = ["uchi", "bnb", "gyu-kaku"];

// Three ways to access an item in an array.
console.log(restaurant[2]);
console.log(restaurant[restaurant.length - 1]);
console.log(restaurant.at(-1));

//Looping through arrays.
//Use for...in... in Python, use for...of... in javascript.

// Ex 1: This is nice for algorithms because it creates an index/counter variable to manipulate
// This is the oldest way and works on anything that is iterable
for (let index = 0; index < restaurant.length; index++) {
  const restaurants = restaurant[index];
  console.log(restaurants);
}

// Ex. 2: This is more like python
for (let restaurants of restaurant) {
  console.log(restaurants);
}

//Looping through objects:

// const student = {
//   name: "Ethan",
//   id: 3,
// };

// This prints out all the keys
for (let key in student) {
  console.log(key);
}
// This prints out the values
for (let key in student) {
  console.log([key]);
}

// Functions - Learn BOTH ways!!!

// Old way
function TwoSum(name, sum, parameter) {}

// Javascript doesn't care if you honor the parameters when you call the function

// ES6 Method of creating functions is assigning it to a const variable:
const ThreeSum = () => {
  console.log("Here is some code");
};

// These two methods of writing functions work the same but they are not the same. They are both vehicles but not the same. It will make more sense when we get to REACT.

// Constants can't be re-assigned, but the memory locations CAN be reassigned.
