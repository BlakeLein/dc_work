# JavaScript

### Putting a JS File into your HTML

- Put a "script" tag in your head and copy your JS code between the tags.
- Link a .js file to your HTML by putting a 'src=""' property in the style tag.
  - Ex: < script src="ecternalDoc.js" ></ script >

**Since HTML reads top to bottom, it's best to put the scripts at the bottom of the document just before the body tag closes.**

### Running JS

- You can run JS in VS code using the "node.js" program. Type 'node filename.js' and run the file (like python)
- You can run javascript in any browser DevTools console.

### Cool points

- console.log() will print the material. console.table() will print the material in a table - GREAT for a dictionary!

### Most common data types:

- Strings
- Numbers (not integers)
- Booleans
- Dates Ex: 'new Date(10, 21, 2015)'
- Null (nothing)
- Array (List in python) **Arrays are considered 'objects' in JS!**
- Object (dictionary in python)
- Function (same as python)

### Concatenating Strings

Two ways to do this:

1. With a plus sign ("hello" + " world!") or ("hello " + variable)
2. Similar to f-strings in python:
   - Ex: console.log(`Hello ${name}`)
   - MUST use back ticks. MUST use $ before each {}

### Three variables

- Var variables: Can be changed; have a global accessibility. This can be unintentionally dangerous!
- Let variables: Can be changed; only exist in the block it was created in (block scope).
- Const variables: CANNOT be changed; only exist in the block it was created in (block scope). Not for for loops.
  - You can change an array even if it's assigned to a const variable, as long as you don't change it's data TYPE.
  - Strings cannot be updated, even if you do not change data types.

### Dynamic Variables

- In JS (unlike many other languages) you can reassign a variable a different data type. This is not always best practice.
- Ex: This is OKAY!

```
var name = "Jane";
name = false;
```

### Value Types

- Strings
- Numbers
- Booleans
- 'undefined'
- 'null'
- NaN
  - This is a number type, but not a number you can use. Returns NaN when you perform an operation between numbers and non-numbers
- Arrays
- Objects
- Classes

Falsey values:

- false
- Empty strings
- null
- undefined
- NaN

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
- The index variable can be accessed outside of the loop as a variable.
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

### Arrays(Lists)

- Add an item to an array with '.push()'; you can add multiple values separated by a comma.
  - .push() does not work on objects.
  - .push() returns the LENGTH of the array; if you console log the .push function, it will return the number of items in the array.
- .pop() will take the last item out of an array
  - .pop() returns the last item of the list, not the length of the list.
- .splice() adds or removes items to an array.
  - .splice(2, 0, "item1", "item2")
    - At index 2, add these two items.
  - .splice(2, 2)
    - At index two, remove two items.
    - Don't need to specify items when removing.

### Objects (Dictionaries)

- Use dot notation to refer to items in an object. Dot notation is only used with objects.
- You could also use brackets

  - console.log(object.name)
  - console.log(object["name"])

- You can use the built-in JS functions Object.keys() or Object.values() to access keys and values
