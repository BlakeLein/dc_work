// function getCoffee() {
//   console.log("Go grab a cup of coffee.");
// }
// getCoffee();

// const getCoffee = new Promise((resolve, reject) => {
//   let coffee = "blonde roast";
//   if (coffee === "black") {
//     resolve("I have your black coffee");
//   } else {
//     reject("I do not have black coffee");
//   }
// });

// console.log(getCoffee.then((message) => console.log(message)));

const functionName = async () => {
  // You fetch from somewhere
  const url = "https://pokeapi.co/api/v2/pokemon";
  // You have to await your fetch
  const response = await fetch(url);
  // You have to convert your response to JSON
  const json = await response.json();
  console.log(json);
};

functionName();

console.log("Hi");
