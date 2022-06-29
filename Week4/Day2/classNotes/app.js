console.log("Testing this link");

// document.
// getElementByID

// One at a time
const button1 = parseInt(document.getElementById("button1").innerText); // This turns the text in the tag to a number - 'parseInt'. Not the 'innerText'
console.log(button1);
console.log(button1 + 400);

const button2 = parseInt(document.getElementById("button2").innerText);
// const button2 = document.getElementById("button2");

// Access when clicked
const addition = document.getElementById("addition");
addition.addEventListener("click", () => console.log("Hey Hey Hey!")); // This will print every time we click. Anonymous funciton necessary so it runs when you click and not just when the page loads

const calculate = () => {};

const calc = document.getElementById("calculate");
calc.onclick = calculate;

const getButtonValue = (buttonInnerText) => {
  console.log(buttonInnerText);
};

// // Simpler
// addition.onclick = () => console.log("Hey, Hey, Hey!");

//By button tags
const buttons = document.getElementsByTagName("button"); // This method automatically creates a list
console.log(buttons);
// This is a list of button tags.
for (const button of buttons) {
  console.log(button.innerText); // Loop through every button tag and displays the inner text.
}
