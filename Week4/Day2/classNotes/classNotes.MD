# DOM Manipulation

- DOM makes all of the HTML a document that the JS can manipulate. It makes the website a document!
- DOM is an object for the document.
- Most of the time we will not be hard coding HTML. Documents would be MASSIVE.
- DOM Manipulation allows use to change a website when certain things happen.
- Layout can stay the same; DOM can let us change the Data.

### Linking JS to document

- Link JS to a page using script tags below the body tags.
- The JS in the HTML is "client-side". The DOM only exists here!
  - If you were to just open up a JS file and run it in node, it has no power to manipulate a document.
  - It becomes client side when you link it to the HTML.

### Accessing Stuff in JS

- Give an element an id in the opening tag.
- Grab that element with that id using the document.getElementById() method.
- Save that to a variable (same name as the id)

1. Grab the whole document. ('document')
2. Grab the element you want ('.getElementById')
3. Grab what part of the element you want ('.innerText')

Dot notation!

### Tracking a mouse click

- Use the event object.
- '.addEventListener('click', what it should do)

  - If you put a function there, you will be calling it and it will just run when the page is loaded. You would need to use an anonymous function (that's created in the addEventListener function) that runs your function WHEN the click happens.
  - Look up some other 'events' that can be used here (other than 'click')

- Could also do '.onClick'

### 'e' Object

- e is an object that you can access that provides all information about an element. Happens only when we have an event.
- It is always the first argument in an event function, no matter what you name it.

ALWAYS USING:

- e.target.innerText
- e.target.name
- e.target.id

### Creating HTML in JS

```
const variable = document.createElement("h1")
variable.innerText = "Hey there"
container.append(variable)
```
