# Handling Browser Events

- And event is an action that happens in the browser!
- When an event occurs the browser produces a signal and provides a listener to execute some codde when the event occurs. (Like clicking a button)
- We use an event handler to react to events.
- `<button onclick="alert("this message")"> </button>` <--- This adds a click event handler to the button.

You can also put it in the JS.

```
<button id="myButton">Click Me!</button>
<script>
  const button = document.querySelector('#myButton')

  button.onclick = function() {
    alert('clicked')
  }
</script>
```

- Grab the button in the HTML by it's ID and assign it to the variable 'button'
- Assign the eventhandler (onclick) to the end of the button variable using DOT NOTATION.
- After the equal sign tell it to execute the anonymous function that does the alerting.

### Things to remember

- If you assign a function to an onclick event with parentheses, it will run when the page loads. If it is a premade function with not parameters, just include the name of the function. If it has parameters, you will need to use an anonymous function.

### addEventListener()

- This has become the standard because you are able to call multiple handlers to the same code.
