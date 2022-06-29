const dropdown = document.getElementById("animal-farm");
console.log(dropdown);
console.log(dropdown.children[0].value); // Accesses the value of the 1st item in the children elements list

// Make a function with conditionals for what to say. Parameters are whatever you are going to select in the dropdown menu.
// dropdown.onchange > Reference the function through an anonymous function that has the event parameter. Pass the parameter event.target.value (what you select.)

////// Add something to the page. //////
// Variable that creates a new container (paragraph).
// Update the inner paragraph text to the value
// Append the paragraph to a div container and it shows up

////// Delete something from the page //////
// set the container to containerVariable.innerHTML = null;
// Clear it at the beginning of the fucntion that receives the onlick!
