const mainContainer = document.getElementById("main-container");
const titleContainer = document.getElementById("title-container");
const links = document.getElementById("links");
const searchArea = document.getElementById("search-area");
const selectBar = document.getElementById("select-bar");
const searchButton = document.getElementById("search-button");
const displayZone = document.getElementById("display-zone");
const titleZone = document.getElementById("title-zone");
const subtitleZone = document.getElementById("subtitle-zone");
const innerDisplay = document.getElementById("inner-display");
const factZone = document.getElementById("fact-zone");
const picZone = document.getElementById("pic-zone");

const clearZones = () => {
  titleZone.innerHTML = null;
  subtitleZone.innerHTML = null;
  factZone.innerHTML = null;
  picZone.innerHTML = null;
};

const showShipName = (name) => {
  const shipName = document.createElement("h1");
  shipName.innerText = `${name}`;
  titleZone.append(shipName);
};

const showShipModel = (name) => {
  const modelName = document.createElement("h2");
  modelName.innerText = `"${name}"`;
  subtitleZone.append(modelName);
};

const showStarshipClass = (name) => {
  const starClass = document.createElement("div");
  starClass.classList = "one";
  let title = document.createElement("p");
  title.classList = "label";
  title.innerText = "Starship Class";
  let value = document.createElement("p");
  value.classList = "value";
  value.innerText = `${name}`;
  starClass.append(title, value);
  factZone.append(starClass);
};

const showManufacturer = (name) => {
  const manufacturer = document.createElement("div");
  manufacturer.classList = "two";
  let title = document.createElement("p");
  title.classList = "label";
  title.innerText = "Manufacturer";
  let value = document.createElement("p");
  value.classList = "value";
  value.innerText = `${name}`;
  manufacturer.append(title, value);
  factZone.append(manufacturer);
};

const showPassengers = (name) => {
  const passengers = document.createElement("div");
  passengers.classList = "three";
  let title = document.createElement("p");
  title.classList = "label";
  title.innerText = "Passenger Potential";
  let value = document.createElement("p");
  value.classList = "value";
  value.innerText = `${name}`;
  passengers.append(title, value);
  factZone.append(passengers);
};

const showCrew = (name) => {
  const crew = document.createElement("div");
  crew.classList = "four";
  let title = document.createElement("p");
  title.classList = "label";
  title.innerText = "Crew Members";
  let value = document.createElement("p");
  value.classList = "value";
  value.innerText = `${name}`;
  crew.append(title, value);
  factZone.append(crew);
};

const showLength = (name) => {
  const length = document.createElement("div");
  length.classList = "five";
  let title = document.createElement("p");
  title.classList = "label";
  title.innerText = "Ship Length";
  let value = document.createElement("p");
  value.classList = "value";
  value.innerText = `${name}`;
  length.append(title, value);
  factZone.append(length);
};

const showHyperdrive = (name) => {
  const hyperdrive = document.createElement("div");
  hyperdrive.classList = "six";
  let title = document.createElement("p");
  title.classList = "label";
  title.innerText = "Hyper Drive Class";
  let value = document.createElement("p");
  value.classList = "value";
  value.innerText = `${name}`;
  hyperdrive.append(title, value);
  factZone.append(hyperdrive);
};

const getSearch = async () => {
  clearZones();
  const selectBarValue = selectBar.value;
  console.log(selectBarValue);
  const url = `https://swapi.dev/api/starships/?search=${selectBarValue}`;
  const shipData = await fetch(url);
  const json = await shipData.json();
  console.log(json);
  console.log(json.results[0].name);
  // Functions to Display Go Here
  if (json.results[0].name == undefined) {
    alert("Please select a ship");
  } else {
    showShipName(json.results[0].name);
    showShipModel(json.results[0].model);
    showStarshipClass(json.results[0].starship_class);
    showManufacturer(json.results[0].manufacturer);
    showPassengers(json.results[0].passengers);
    showCrew(json.results[0].crew);
    showLength(json.results[0].length);
    showHyperdrive(json.results[0].hyperdrive_rating);
  }
};
const getOptions = async () => {
  const url = `https://swapi.dev/api/starships/`;
  const shipData = await fetch(url);
  const json = await shipData.json();
  console.log(json);
  console.log(json.results.length);
  for (let i = 0; i < json.results.length; i++) {
    let newOption = document.createElement("option");
    newOption.innerText = json.results[i].name;
    selectBar.append(newOption);
  }
};

getOptions();
searchButton.onclick = () => getSearch();
