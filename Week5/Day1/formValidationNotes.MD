# Form Validation

- The practice of checking if user-entered data is the correct format.
- Should be done on client and server side.

### HTML Input Validations

- HTML input tags can be assigned a "type". These types will help police for desired input.
  - Type "email": Will throw an error message if there is no @
  - Type "number": Will throw an error message if you enter anything other than a number.
  - Type "password": Will hide the input as the user types. You can also add the "minlength" and "maxlength" attributes to throw error messages as well (these can be applied to any text-based input.)
- The "required" attribute can be given to an input tag that prevents the page from moving forward until they enter for that field.
<hr>

### Regular Expression ("Regex")

- A special text string for describing a search pattern.
- You can use regex in JS' string methods to match a pattern and modify a string.
- You can use the "pattern" attribute in an input tag. What you assign that attribute is what the user must type exactly for it to be correct.
  - Another example of the pattern attribute is: pattern="[A-Za-z0-9]{4-12}" - This means that you can only enter letters (capital or lower case) between a and z as well as numbers between 0 and 9. The second part of the attribute value means that the input must be between 4 and 12 characters long. (You could put a + instead to unrestrict the length)
  <hr>

### Regular Expressions in JavaScript

- In JavaScript, a regular expression is a type of object.
- It can be either constructed with the "regex constructor" or written as a literal calue by enclosing a pattern in forward slash "/" characters

```
let regularExpressionConstructor = new RegExp("abc")
let regularExpressionLiteral = /abc/
```

**Use the literal method if you expect the regex to be constant**

- Here is an example of how to use regex in JS. The .test() method allows us to pass a string argument and compare it to the regex variable we assigned.

```
const myRegex = /Hello World/
const test = myRegex.test("Hello World")
```

- We can use string methods to update our variable based on our pattern.

```
const myRegex = /\s/
const myString = "Hello World"

const newString = myString.replace(myRegex, "-")
```

- Here's a breakdown of this code:

  - The '\s' is a special character (like '\n' or '\t') that refers to white space in a string.
  - The .replace() method allows us to replace anything in the string ("first argument", in this case: whitespace) with something different ("second argument", in thios case a dash).
  - If you console log the newString variable, you will have "Hello-World".

**You would need to add the 'g' modifier to the regex value if you wanted to check for ALL instances of whitespace in the string (/\s/g)**

### Using JS for Form Validation

- In the JS code, add an event listener to a submission that runs a "check" function when a user submits their input.
- This check function can return a boolean value based on if it meets the regex standards.
- If the return is false, you can reject the input and flag an alert.

**This is a great way to have even more validated input! What goes beyond simple HTML validations.**

### Constraint Validation API

- You can use constraint validation API (a system supported by most browsers) for form control.
- One example would be to use this for providing a user with custon error messages with the setCustonValidity() method provided by this API. This method changes the built-in HTML error message to whatever we decide.
- Example:

```
<script>
  const form = document.querySelector("form");
  const nameInput = document.querySelector("#name");

  function checkName() {
    const myRegex = /[A-Za-z]+/;
    if (!myRegex.test(nameInput.value)) {
      nameInput.setCustomValidity(
        "Please use only lowercase or uppercase letters"
      );
    } else {
      nameInput.setCustomValidity("");
    }
  }
  nameInput.addEventListener("change", checkName, false);
</script>
```
