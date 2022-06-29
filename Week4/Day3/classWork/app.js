// ternary operator ?
// const data = iftruthy ? do this : else do this if false

const admin = "Joe";
const username = admin === "Joe" ? "jwfrasier" : "rrozier";

console.log(username);
// This tests to see if a variable is one thing. If it is change it to the thing after the ?; otherwise change it to the thing after
// the colon.

// const username = admin === "Joe" ? "jwfrasier" : null;
// // Short hand for this is using the AND operator
// const loggedIn = admin === "Joe" && "jwfrasier";

// The OR Operator || (called pipes)
// const permittedToStay = loggedIn || "child";
// If the first one is true it takes that, otherwise it's the second one.
// This is a useful tool to safeguard variables; sort of a default option. In the above example, "child" would be the default if
// the first thing was falsey.

// Combining two arrays
const array1 = ["andrea", "amanda", "jason"];
const array2 = ["west", "rahmin", "rahmin's mother"];
// const students = array1.concat(array2);
// console.log(students);

// OR USE SPREAD OPERATOR
students = [...array1, ...array2];
console.log(students);

const notANumber = "1";
console.log(typeof notANumber);
// The plus sign makes it a number instead of a string. Unary Operator
console.log(typeof +notANumber);

// .toUpperCase or .toLowerCase

// forEach for loop is built for arrays. "For each thing in this array, we are going to do something"
// students.forEach((element) => {
//   console.log(element.toUpperCase);
// });

/*.map() performs a function on each element in an array and returns everything you did into one new array.
The argument is anonymous, so you have to give it something. Name it something singular.
If you do all your JS logic in one line, you don't need curlies or a return statement. It's infering. */
const upperCasedStudents = students.map((student) => {
  return student.toUpperCase();
});
console.log(upperCasedStudents);
/* You can do as much logic as you can in a map function. It will perform it on each item of the list.
MUST HAVE A RETURN STATEMENT BECAUSE IT'S MORE THAN ONE LINE OF CODE. */

const googleEmployee = {
  name: "Sundar Pichai",
  status: "Ceo",
  salary: "$1 billion",
};

const noogleEmployee = {
  name: "Carlos",
  status: "noogler",
  salary: "not a billion",
  department: "google cloud",
};

const allGoogleEmployees = [googleEmployee, noogleEmployee];
/* These objects have similar keys but not all the same. This will check if the department key is there first before it prints to
avoid any unwanted 'undefined' statemnts on the website.*/
allGoogleEmployees.forEach((emp) => {
  console.log(emp?.department);
});
/* If 'department' were a dictionary or list, you can use bracket or dot-notation to access the specific item. The ?
will keep the code for breaking. This is an optional chain. */
