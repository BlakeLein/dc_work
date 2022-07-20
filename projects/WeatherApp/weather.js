const API_KEY = "";
const displayZone = document.getElementById("display");
displayZone.classList = "display-box";
const searchButton = document.getElementById("search");
const searchZone = document.getElementById("search-container");
const fullContainer = document.getElementById("main");
const innerContainer = document.getElementById("inner-container");
const searchInput = document.getElementById("input");

const showCityAndTemp = (name, ele) => {
  const city = document.createElement("div");
  city.classList = "item";
  let cityName = document.createElement("p");
  cityName.innerText = `${name}`;
  cityName.classList = "city-name";
  let value = document.createElement("p");
  value.classList = "temp-value";
  value.innerText = `${ele.toFixed(0)}°`;
  city.append(cityName, value);
  displayZone.append(city);
};

const showIcon = (icon) => {
  const iconItem = document.createElement("div");
  iconItem.classList = "item";
  let cityIcon = document.createElement("img");
  cityIcon.src = `http://openweathermap.org/img/wn/${icon}@2x.png`;
  iconItem.append(cityIcon);
  displayZone.append(iconItem);
};

const showHighLow = (low, high) => {
  const highLow = document.createElement("div");
  highLow.classList = "item";
  let name = document.createElement("p");
  name.innerText = "High and Low";
  name.classList = "other-name";
  let value = document.createElement("p");
  value.innerText = `${low.toFixed(0)}° / ${high.toFixed(0)}°`;
  value.classList = "other-value";
  highLow.append(name, value);
  displayZone.append(highLow);
};

const showFeelsLike = (ele) => {
  const feelsLike = document.createElement("div");
  feelsLike.classList = "item";
  let name = document.createElement("p");
  name.innerText = "Feels Like";
  name.classList = "other-name";
  let value = document.createElement("p");
  value.innerText = `${ele.toFixed(0)}°`;
  value.classList = "other-value";
  feelsLike.append(name, value);
  displayZone.append(feelsLike);
};

const showHumidity = (ele) => {
  const humidity = document.createElement("div");
  humidity.classList = "item";
  let name = document.createElement("p");
  name.innerText = "Humidity";
  name.classList = "other-name";
  let value = document.createElement("p");
  value.innerText = `${ele}%`;
  value.classList = "other-value";
  humidity.append(name, value);
  displayZone.append(humidity);
};

const showWindSpeed = (wind, gust) => {
  const windSpeed = document.createElement("div");
  windSpeed.classList = "item";
  let name = document.createElement("p");
  name.innerText = "Wind Speed";
  name.classList = "other-name";
  let value = document.createElement("p");
  value.innerText = `${wind.toFixed(1)} mph`;
  value.classList = "other-value";
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
    showCityAndTemp(json.name, json.main.temp);
    showIcon(json.weather[0].icon);
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
