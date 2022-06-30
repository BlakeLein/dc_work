const divs = document.querySelectorAll("div");
const buttons = document.querySelectorAll("button");

const colors = [
  "blue",
  "green",
  "red",
  "purple",
  "yellow",
  "orange",
  "pink",
  "black",
  "brown",
  "gray",
  "darkblue",
  "lightpink",
  "yellowgreen",
  "violet",
  "aqua",
  "magenta",
];

for (let s = 0; s < divs.length; s++) {
  buttons[s].addEventListener("click", () => {
    if (divs[s].style.backgroundColor === "white") {
      divs[s].style.backgroundColor = colors[s];
      buttons[s].innerText = `I'm ${colors[s].toUpperCase()}!`;
    } else {
      divs[s].style.backgroundColor = "white";
      buttons[s].innerText = "What Color Am I?";
    }
  });
}
