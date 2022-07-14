// HTML Grabs
const body = document.getElementById("body");
const button = document.getElementById("button");
const select = document.getElementById("select");
const displayZone = document.getElementById("display-zone");
const titleZone = document.getElementById("title-zone");

// Collapsable NavBar Fucntions
function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("menu-button").style.marginLeft = "250px";
}
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("menu-button").style.marginLeft = "0";
}

const randomImage = () => {
  let x = Math.floor(4 * Math.random());

  body.style.backgroundImage = `url(./images/bg${x}.jpg)`;
  body.style.backgroundRepeat = "no-repeat";
  body.style.backgroundSize = "cover";
};
