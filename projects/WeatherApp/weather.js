// const API_KEY =
const displayZone = document.getElementById("display");
displayZone.classList = "display-box";
const searchButton = document.getElementById("search");
const searchZone = document.getElementById("search-container");
const fullContainer = document.getElementById("main");
const innerContainer = document.getElementById("inner-container");
const searchInput = document.getElementById("input");

const showCity = (name, icon) => {
  const city = document.createElement("div");
  city.classList = "item";
  let cityName = document.createElement("p");
  cityName.innerText = `${name}`;
  let cityIcon = document.createElement("img");
  cityIcon.src = `http://openweathermap.org/img/wn/${icon}@2x.png`;
  city.append(cityName, cityIcon);
  displayZone.append(city);
};

const showTemp = (ele) => {
  const message = document.createElement("div");
  message.classList = "item";
  let name = document.createElement("p");
  name.innerText = "Current Temperature";
  let value = document.createElement("p");
  value.innerText = `${ele.toFixed(1)}°`;
  message.append(name, value);
  displayZone.append(message);
};

const showHighLow = (low, high) => {
  const highLow = document.createElement("div");
  highLow.classList = "item";
  let name = document.createElement("p");
  name.innerText = "High and Low";
  let value = document.createElement("p");
  value.innerText = `${low.toFixed(1)}° / ${high.toFixed(1)}°`;
  highLow.append(name, value);
  displayZone.append(highLow);
};

const showFeelsLike = (ele) => {
  const feelsLike = document.createElement("div");
  feelsLike.classList = "item";
  let name = document.createElement("p");
  name.innerText = "Feels Like";
  let value = document.createElement("p");
  value.innerText = `${ele.toFixed(1)}°`;
  feelsLike.append(name, value);
  displayZone.append(feelsLike);
};

const showHumidity = (ele) => {
  const humidity = document.createElement("div");
  humidity.classList = "item";
  let name = document.createElement("p");
  name.innerText = "Humidity";
  let value = document.createElement("p");
  value.innerText = `${ele}%`;
  humidity.append(name, value);
  displayZone.append(humidity);
};

const showWindSpeed = (wind, gust) => {
  const windSpeed = document.createElement("div");
  windSpeed.classList = "item";
  let name = document.createElement("p");
  name.innerText = "Wind Speed";
  let value = document.createElement("p");
  value.innerText = `${wind.toFixed(1)} mph`;
  windSpeed.append(name, value);
  displayZone.append(windSpeed);
};
const searchWeather = async () => {
  displayZone.innerHTML = null;
  const searchInputValue = searchInput.value;
  const url = `http://api.openweathermap.org/data/2.5/weather?q=${searchInputValue},us&units=imperial&id=524901&appid=${API_KEY}`;
  const weatherData = await fetch(url);
  const json = await weatherData.json();
  console.log(json);
  if (json.name == undefined) {
    alert("Please enter a valid US City Name or Zip Code.");
  } else {
    // console.log(navigator.geolocation.getCurrentPosition(success));
    showCity(json.name, json.weather[0].icon);
    showTemp(json.main.temp);
    showHighLow(json.main.temp_min, json.main.temp_max);
    showFeelsLike(json.main.feels_like);
    showHumidity(json.main.humidity);
    showWindSpeed(json.wind.speed, json.wind.gust);
  }
};

searchButton.onclick = () => searchWeather();
searchInput.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    event.preventDefault();
    searchWeather();
  }
});

const randomImage = () => {
  let images = [
    "./images/1.jpg",
    "./images/2.jpg",
    "./images/3.jpg",
    "./images/4.jpg",
    "./images/5.jpg",
    "./images/6.jpg",
    "./images/7.jpg",
    "./images/8.jpg",
    "./images/9.jpg",
    "./images/10.jpg",
    "./images/11.jpg",
  ];
  let size = images.length;
  let x = Math.floor(size * Math.random());

  fullContainer.style.backgroundImage = `url(./images/${x}.jpg)`;
  fullContainer.style.backgroundRepeat = "no-repeat";
  fullContainer.style.backgroundSize = "cover";
};
