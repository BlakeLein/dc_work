// Small 1
const heading = document.getElementById("heading");
heading.innerText = "Toppings";

// Small 2
const burger = document.getElementById("burger");
burger.className = "list-item";

// Small 3
const newItem = document.createElement("li");
newItem.innerText = "Bun";
document.getElementById("list").append(newItem);
