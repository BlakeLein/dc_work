// Exercise 1
// Write a madlib function, which is given a name and a subject. It will return(not print) a new string: (name)'s favorite subject in school is (subject).

// Old way
// function madLib(name, subject) {
//   return `${name}'s favorite subject in school is ${subject}.`;
// }

// console.log(madLib("Blake", "Programming"));

// // New Way
// const madLib = (name, subject) => {
//   return `${name}'s favorite subject in school is ${subject}.`;
// };

// console.log(madLib("Blake", "Programming"));

//Exercise 2
// Write a function tipAmount that is given the bill amount and the level of service (one of good, fair and poor) and returns the dollar amount for the tip. Based on:

// Old Way
// function tipAmount(bill, service) {
//   if (service === "good") {
//     return bill + bill * 0.2;
//   } else if (service === "fair") {
//     return bill + bill * 0.15;
//   } else if (service === "bad") {
//     return bill + bill * 0.1;
//   }
// }

// console.log(tipAmount(20, "good"));

// New Way
// const tipAmount = (bill, service) => {
//   if (service === "good") {
//     return bill + bill * 0.2;
//   } else if (service === "fair") {
//     return bill + bill * 0.15;
//   } else if (service === "bad") {
//     return bill + bill * 0.1;
//   }
// };
// console.log(tipAmount(20, "good"));

//Exercise 3
// Write a function totalAmount that takes the same arguments as tipAmount except it returns the total as the tip amount plus the bill amount. This function may make use of tipAmount as a sub-task
// I did this above.

// Exercise 3B
// const splitAmount = (bill, service, people) => {
//   if (service === "good") {
//     bill += bill * 0.2;
//   } else if (service === "fair") {
//     bill += bill * 0.15;
//   } else if (service === "bad") {
//     bill += bill * 0.1;
//   }
//   return bill / people;
// };

// console.log(splitAmount(20, "good", 6));

// Hello You!
// const hello = (name) => {
//   console.log(`Hello ${name}!`);
// };

// hello("Blake");

// Hello You with default:
// const hello = (name) => {
//   if (name) {
//     console.log(`Hello ${name}!`);
//   } else {
//     console.log(`Hello world!`);
//   }
// };
// hello();

// Print Numbers
// Write a function printNumbers which is given a start number and an end number. It will print the numbers from one to the other, one per line:

// Old Way
// function printNumbers(start, end) {
//   for (let i = start; i <= end; i++) {
//     console.log(i);
//   }
// }

// printNumbers(2, 5);

// New Way
// const printNumbers = (start, end) => {
//   for (let i = start; i <= end; i++) {
//     console.log(i);
//   }
// };

// printNumbers(2, 5);

//Exercise 4
// Write a function printSquare which is given a size and prints a square of that size using asterisks.
// Old way
// function printSquare(size) {
//   for (let i = 1; i <= size; i++) {
//     let box = "";
//     for (let j = 1; j <= size; j++) {
//       console.log("*");
//     }
//     console.log("*");
//   }
// }
// printSquare(6);
