# DOM (Document Object Model)

## What is the DOM?

- Primary way JS interacts with a web page.
- The browser provides a `document` variable that has properties and methods you can use to make changes to a page.

## DOM vs BOM

- The Browser Object Model represents the window or tab that shows the page.
- The BOM is accessed through the `window` variable. This variable has a `document` property.
  - This variable also has `history`, `screen`, and `location` properties
  - Examples:
    - `window.screen` contains information about a user's browser, including the width and height properties.
    - `window.screen.width` gives you the current width of the browser's window. (Can also be written as just `screen.width`)
- The BOM (window) contains the DOM (document)

## Node Tree

- The primary job of the browser is to convert an HTML document into a DOM.
- The DOM Structure is represented by the 'Node Tree'.
  - Each element, attribute, property, or anything can be nodes and accessed in the DOM model.

## Accessing the DOM

- The `document` interface represents any web page loaded in the broswer and serves as an entry point into the web page's node tree.

### DOM Selectors

- DOM selectors are used to access HTML elements within a document.
- The following selector methods are properties of the document object. We prefix these selectors with the `document` to call them.

  - `getelementbynametag('p')` : searches the HTML document for `p` tags and returns a list of these elements in an `HTMLCollection` Object.
  - `getElementsByClassName('link')` : returns all the elements that match the specified `class` name in an `HTMLCollection` Object.
  - `getElementById('password')` : returns the first element that its id matches the given string.
  - `querySelector('#password')` : returns the first element that matches the specified CSS selector
  - `querySelectorAll('.link')` : returns all the elements that match the specified CSS selector in a `NodeList`

  All these methods return either an `element`, an `HTMLCollection` (Object of elements only), or a `NodeList` (list of any node, not just elements).

### Application (See HTML and JS Files)

**Ex 1**

```
const heading = document.getElementById("heading");
```

- `getElementById()` searches the HTML for an `id` that matches the given string and returns that element. In this case, `getElementById()` returns the `h1` element because `getElementById()` is looking for the element with the `id` matching 'heading.'
  - `getElementById()` is a function.
  - The function RETURNS the element matching the string you pass it. Now we are accessing the heading.

**Ex 2**

```
const listItems = document.getElementsByTagName("li");
```

- `getElementsByTagName()` returns an array-like object called a `HTMLCollection` object. In this example, we are selecting all the `li` elements.

**Ex 3**

```
const listItemsByClass = document.querySelectorAll(".nav-link");
```

- `querySelectorAll()` method returns a `NodeList` object.
  - `NodeList` is similar to an `HTMLCollection`, though it is possible to iterate over it with `forEach()`. This must be beneficial!
  - Any element that matches the specified class 'nav-link' will be added to the `NodeList`.
  - Both `querySelector()` and `querySelectorAll()` are passed a string that uses a CSS specifier. In the example above we are using the "." to specify we are looking for the class of 'nav-link'.

### Element Properties

- Elements we grab from the Document can be manipulated with different properties. Here are some examples ---

- (Example 4): Here we are accessing information stored in the object's `innerText` property and assigning it to a variable. In this case, If we were to `console.log(headingText)`, it would output to the console 'Navigation'.

```const heading = document.getElementById("heading");
const headingText = heading.innerText;
```

- (Example 5): Another useful property is `length`. This returns a `NodeList`, and since there are three elements, the return is 3.

```
const listItemsByClass = document.querySelectorAll(".nav-link");
const listItemsLength = listItemsByClass.length;
```

### Changing the DOM

- With JS, we don't just access the nodes of the information with the DOM; we can also update it and create new elements.

### Updating the DOM

- If we wanted to change the text of a heading, we could assigning `document.querySelector('#heading')` to a variable will allow us to access the innerText property of the element. We can then reassigned the value of the innerText property.

```
const heading = document.querySelector("#heading");
heading.innerText = "Links";
```

- We can also change an element's style. Let's change the `style` property of our `h1` element:

```
const heading = document.querySelector('#heading')
heading.innerText = "Links"
heading.style.color = "rgb(255, 0,0)"
```

1. Access the heading with the `documnet.querySelector('#heading')` method.
2. Changes the inner text to 'Links'
3. The `style` and `color` properties are accessed and you set that equal to the new desired color.

### Creating Elements

You can create an entire page with just JS code. Here is how we could recreate the html with just JS. This will update the HTML for you

- For creating the different elements we can use the `createElement()` method. Lets go ahead and make one for each of the elements we need to complete our bar.

```
<script>
const headerElement = document.createElement('h1')
const listElement = document.createElement('ul')

const listItemOne = document.createElement('li')
const listItemTwo = document.createElement('li')
const listItemThree = document.createElement('li')
</script>
```

- `createElement()` method creates the HTML element specified by `tagName`. Here we've created elements for `h1`, `ul` and three `li`s. Now that we have created them let's put them in our document. First we will create a `div` in our HTML with an `id` of 'root'.
- In our `<script>`, we can add a selector for the root `div`. To add the new elements to the DOM we need to use the `append()` method; this inserts a set of node objects or DOMString objects after the last child of the ParentNode.

```
const headerElement = document.createElement('h1')
const listElement = document.createElement('ul')

const listItemOne = document.createElement('li')
const listItemTwo = document.createElement('li')
const listItemThree = document.createElement('li')

const root = document.querySelector('#root')

root.append(headerElement)
root.append(listElement)
```

1. Create the `header`, `list`, and `list` items in the first 5 lines.
2. Assign the div we created (our ParentNode) to a variable called `root`
3. Append the elements to the parent node.
4. We could then append the list items to the list with the code below. Notice that we can append multiple things at once!

```
listElement.append(listItemOne, listItemTwo, listItemThree)
```

- Using JS only, we can now add some text to our elements with our `innerText` property:

```
headerElement.innerText = "Navigation"
listItemOne.innerText = "Home"
listItemTwo.innerText = "Store"
listItemThree.innerText = "Contact"
```

### Adding Attributes

- We can add `id` or `class` attributes to our elements.

```
headerElement.id = "heading"
listElement.id = "nav-list"
```

- The childNodes() method will return a NodeList of all the elements that are children of a chosen element. This is helpful if we want to add the same attribute to mutliple child elements as possible.

```
listElement.childNodes.forEach(item => {
  item.className = "nav-link"
})
```

- The `childNodes()` method returns a NodeList of our child elements, so we have to use the `forEach()` methid to apply the class to each item one-at-a-time.
- We use `className` because class is a JS keyword.
