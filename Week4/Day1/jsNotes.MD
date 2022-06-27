# JavaScript

### Putting a JS File into your HTML

- Put a "script" tag in your head and copy your JS code between the tags.
- Link a .js file to your HTML by putting a 'src=""' property in the style tag.
  - Ex: < script src="ecternalDoc.js" ></ script >

**Since HTML reads top to bottom, it's best to put the scripts at the bottom of the document just before the body tag closes.**

### Running JS

- You can run JS in VS code using the "node.js" program. Type 'node filename.js' and run the file (like python)
- You can run javascript in any browser DevTools console.

### Most common data types:

- Strings
- Numbers (not integers)
- Booleans
- Dates Ex: 'new Date(10, 21, 2015)'
- Null (nothing)
- Array (List in python)
- Object (dictionary in python)
- Function (same as python)

### Concatenating Strings

Two ways to do this:

1. With a plus sign ("hello" + " world!") or ("hello " + variable)
2. Similar to f-strings in python:
   - Ex: console.log(`Hello ${name}`)
   - MUST use back ticks. MUST use $ before each {}

### Dynamic Variables

- In JS (unlike many other languages) you can reassign a variable a different data type. This is not always best practice.
- Ex: This is OKAY!

```
var name = "Jane";
name = false;
```

### Operators

- Assignment =
- Addition +
- Subraction -
- Increment ++
- Decrement --
- Multiplication \*
- Division /
- Modulus (Division Remainder) %
- Loose Comparison ==
- Strict Comparison ===
- Not !
- And &&
- Or ||

### Functions

- Written a bit differently, called the same.
- Can accept parameters
- Stops running when it encounters a 'return' statement.

## Conditionals

### If Statements

- Uses the if, else if, and else statements (no 'elif')
- The comparison logic is wrapped in parentheses after the key word.
- Note the use of curly braces instead of colons and indentations

```
if (age < 18) {
    here is some code
} else if (age < 30) {
    here is even more code
} else {
    last bit of code
}
```

### 'Switch Case' Statement

- Used for making a single comparison against multiple pieces of data. This can be done with an "if" statement, but is more concise and better legibility.
- You provide and expression by passing data into the switch, then the case presents a piece of data to compare to the switch expression. If the switch expression matches the case the code block is executed, if the comparison doesn't match the code block is skipped.

```
var day; // Start by declaring the variable here.

switch (new Date().getDay()) { // Declare switch function. Paretheses takes arguments to compare. All in curly braces.
// Checks the day against each option. New case# for each (start with 0)
  case 0:
    day = "Sunday";
    break;
  case 1:
    day = "Monday";
    break; // Include break statement after each.
  case 2:
    day = "Tuesday";
    break;
  case 3:
    day = "Wednesday";
    break;
  case 4:
    day = "Thursday";
    break;
  case 5:
    day = "Friday";
    break;
  case 6:
    day = "Saturday";
    break;
  default:
    console.log("Can't figure out day");
} // Default is if there is no match. Put last.

console.log(`Today is ${day}`);
```

## Loops

### For Loops

To create a for loop, you have to set a base number and increment through it until the expression is false. Like a mini while loop logic inside of the loop logic:

```
for (i = 0; i < 10; i++) {
    console.log(i)
}
```

- Set the counter variable (i), while i is less than 10, then increment i one value. The code block iterates as these parameters allow.
- Think:

1. Define counter!
2. Set boundaries on counter!
3. Increment!

### While Loops

Similar to python, while loops rely on booleans. While an expression is true, perform the code block:

```
var x = 0;
while (x < 10) {
do this code
x++ //Increment x to avoid infinite loop
}
```
