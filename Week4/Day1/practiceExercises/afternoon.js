// EXERCISE 1
// function lvl5exercise1() {
//   // Push the string "hello" into the array and return the array
//   var arr = [1, "adam"];
//   arr.push("hello");
//   console.log(arr);
// }
// lvl5exercise1();

// function lvl5exercise2() {
//   // Remove the last element from the array and return the array
//   var arr = [1, "adam"];
//   arr.pop();
//   console.log(arr);
// }

// lvl5exercise2();

// function lvl5exercise3() {
//   // Return the length of the array
//   var arr = [1, "adam"];
//   console.log(arr.length);
// }

// lvl5exercise3();

// function lvl5exercise4() {
//   // Return the index of item "adam" in the array
//   var arr = [1, "adam"];
//   console.log(arr.indexOf("adam"));
// }

// lvl5exercise4();

// EX 2 -- USE A SWITCH STATEMENT HERE.
// function lvl6exercise1(num) {
//   // Return 'hello' if num is 1, 'world' if num is 2, otherwise return 'bye'
//   switch (num) {
//     case 1:
//       return "hello";
//       break;
//     case 2:
//       return "world";
//       break;
//     default:
//       return "bye";
//   }
// }
// console.log(lvl6exercise1(1));

// function lvl6exercise2() {
//   // Push 10 'hello' strings into the array using a for loop, then return it
//   var arr = [];
//   for (index = 1; index <= 10; index++) {
//     arr.push("hello");
//   }
//   return arr;
// }

// console.log(lvl6exercise2());

// function lvl6exercise3() {
//   // Empty this array using a while loop and return it
//   var arr = [
//     "hello",
//     "hello",
//     "hello",
//     "hello",
//     "hello",
//     "hello",
//     "hello",
//     "hello",
//     "hello",
//     "hello",
//   ];
//   while (arr.length > 0) {
//     arr.pop();
//   }
//   return arr;
// }

// console.log(lvl6exercise3());

// EX 3
// Write a function that takes a number as an input.
// Have it create an empty array and then push a string into the array as many
// times as the input number. If the input is anything other than a positive
// integer return an empty array
//
// Name the function "finalFunction"

// const finalFunction = (num) => {
//   let arr = [];
//   if (num <= 0) {
//     return arr;
//   } else if (num > 0) {
//     for (let i = 1; i <= num; i++) {
//       arr.push("Here's a string.");
//     }
//     return arr;
//   }
// };

// console.log(finalFunction(0));

// Write a function called mul

function mul(a) {
  // Anonymous function
  return function (b) {
    //Anonymous function
    return function (c) {
      return a * b * c;
    };
  };
}
console.log(multiply(2)(3)(4));

/* The anonymous functions are only there to support the main function. They don't exist otherwise.
The is called currying. It's used to break up arguments so you have access to one of them at a time.
The first parenthetical argument is the mul functions parameter; the second parenthetical argument is for the
first anonymous function; and so forth.
*/
