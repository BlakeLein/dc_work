const square1 = document.getElementById("one");
const square2 = document.getElementById("two");
const square3 = document.getElementById("three");
const square4 = document.getElementById("four");
const square5 = document.getElementById("five");
const square6 = document.getElementById("six");
const square7 = document.getElementById("seven");
const square8 = document.getElementById("eight");
const square9 = document.getElementById("nine");
const square10 = document.getElementById("ten");
const square11 = document.getElementById("eleven");
const square12 = document.getElementById("twelve");
const square13 = document.getElementById("thirteen");
const square14 = document.getElementById("fourteen");
const square15 = document.getElementById("fifteen");
const square16 = document.getElementById("sixteen");

const squares = [
  square1,
  square2,
  square3,
  square4,
  square5,
  square6,
  square7,
  square8,
  square9,
  square10,
  square11,
  square12,
  square13,
  square14,
  square15,
  square16,
];

const button1 = document.getElementById("button1");
const button2 = document.getElementById("button2");
const button3 = document.getElementById("button3");
const button4 = document.getElementById("button4");
const button5 = document.getElementById("button5");
const button6 = document.getElementById("button6");
const button7 = document.getElementById("button7");
const button8 = document.getElementById("button8");
const button9 = document.getElementById("button9");
const button10 = document.getElementById("button10");
const button11 = document.getElementById("button11");
const button12 = document.getElementById("button12");
const button13 = document.getElementById("button13");
const button14 = document.getElementById("button14");
const button15 = document.getElementById("button15");
const button16 = document.getElementById("button16");

const buttons = [
  button1,
  button2,
  button3,
  button4,
  button5,
  button6,
  button7,
  button8,
  button9,
  button10,
  button11,
  button12,
  button13,
  button14,
  button15,
  button16,
];

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

for (let s = 0; s < squares.length; s++) {
  buttons[s].addEventListener("click", () => {
    if (squares[s].style.backgroundColor === "white") {
      squares[s].style.backgroundColor = colors[s];
      buttons[s].innerText = `I'm ${colors[s]}!`;
    } else {
      squares[s].style.backgroundColor = "white";
      buttons[s].innerText = "What Color Am I?";
    }
  });
}

//   button1.addEventListener("click", () => {
//     if (square1.style.backgroundColor === "white") {
//       square1.style.backgroundColor = "blue";
//       button1.innerText = "I'm Blue!";
//     } else {
//       square1.style.backgroundColor = "white";
//       button1.innerText = "What Color Am I?";
//     }
//   });

//   button2.addEventListener("click", () => {
//     if (square2.style.backgroundColor === "white") {
//       square2.style.backgroundColor = "green";
//       button2.innerText = "I'm Green!";
//     } else {
//       square2.style.backgroundColor = "white";
//       button2.innerText = "What Color Am I?";
//     }
//   });
//   button3.addEventListener("click", () => {
//     if (square3.style.backgroundColor === "white") {
//       square3.style.backgroundColor = "red";
//       button3.innerText = "I'm Red!";
//     } else {
//       square3.style.backgroundColor = "white";
//       button3.innerText = "What Color Am I?";
//     }
//   });
//   button4.addEventListener("click", () => {
//     if (square4.style.backgroundColor === "white") {
//       square4.style.backgroundColor = "purple";
//       button4.innerText = "I'm Purple!";
//     } else {
//       square4.style.backgroundColor = "white";
//       button4.innerText = "What Color Am I?";
//     }
//   });
//   button5.addEventListener("click", () => {
//     if (square5.style.backgroundColor === "white") {
//       square5.style.backgroundColor = "yellow";
//       button5.innerText = "I'm Yellow!";
//     } else {
//       square5.style.backgroundColor = "white";
//       button5.innerText = "What Color Am I?";
//     }
//   });
//   button6.addEventListener("click", () => {
//     if (square6.style.backgroundColor === "white") {
//       square6.style.backgroundColor = "orange";
//       button6.innerText = "I'm Orange!";
//     } else {
//       square6.style.backgroundColor = "white";
//       button6.innerText = "What Color Am I?";
//     }
//   });
//   button7.addEventListener("click", () => {
//     if (square7.style.backgroundColor === "white") {
//       square7.style.backgroundColor = "pink";
//       button7.innerText = "I'm Pink!";
//     } else {
//       square7.style.backgroundColor = "white";
//       button7.innerText = "What Color Am I?";
//     }
//   });
//   button8.addEventListener("click", () => {
//     if (square8.style.backgroundColor === "white") {
//       square8.style.backgroundColor = "black";
//       button8.innerText = "I'm Black!";
//     } else {
//       square8.style.backgroundColor = "white";
//       button8.innerText = "What Color Am I?";
//     }
//   });
//   button9.addEventListener("click", () => {
//     if (square9.style.backgroundColor === "white") {
//       square9.style.backgroundColor = "brown";
//       button9.innerText = "I'm Brown!";
//     } else {
//       square9.style.backgroundColor = "white";
//       button9.innerText = "What Color Am I?";
//     }
//   });
//   button10.addEventListener("click", () => {
//     if (square10.style.backgroundColor === "white") {
//       square10.style.backgroundColor = "gray";
//       button10.innerText = "I'm Gray!";
//     } else {
//       square10.style.backgroundColor = "white";
//       button10.innerText = "What Color Am I?";
//     }
//   });
//   button11.addEventListener("click", () => {
//     if (square11.style.backgroundColor === "white") {
//       square11.style.backgroundColor = "darkblue";
//       button11.innerText = "I'm Dark Blue!";
//     } else {
//       square11.style.backgroundColor = "white";
//       button11.innerText = "What Color Am I?";
//     }
//   });
//   button12.addEventListener("click", () => {
//     if (square12.style.backgroundColor === "white") {
//       square12.style.backgroundColor = "lightpink";
//       button12.innerText = "I'm Rose!";
//     } else {
//       square12.style.backgroundColor = "white";
//       button12.innerText = "What Color Am I?";
//     }
//   });
//   button13.addEventListener("click", () => {
//     if (square13.style.backgroundColor === "white") {
//       square13.style.backgroundColor = "yellowgreen";
//       button13.innerText = "I'm Light Green!";
//     } else {
//       square13.style.backgroundColor = "white";
//       button13.innerText = "What Color Am I?";
//     }
//   });
//   button14.addEventListener("click", () => {
//     if (square14.style.backgroundColor === "white") {
//       square14.style.backgroundColor = "violet";
//       button14.innerText = "I'm Violet!";
//     } else {
//       square14.style.backgroundColor = "white";
//       button14.innerText = "What Color Am I?";
//     }
//   });
//   button15.addEventListener("click", () => {
//     if (square15.style.backgroundColor === "white") {
//       square15.style.backgroundColor = "aqua";
//       button15.innerText = "I'm Aqua!";
//     } else {
//       square15.style.backgroundColor = "white";
//       button15.innerText = "What Color Am I?";
//     }
//   });
//   button16.addEventListener("click", () => {
//     if (square16.style.backgroundColor === "white") {
//       square16.style.backgroundColor = "magenta";
//       button16.innerText = "I'm Magenta!";
//     } else {
//       square16.style.backgroundColor = "white";
//       button16.innerText = "What Color Am I?";
//     }
//   });
// }
