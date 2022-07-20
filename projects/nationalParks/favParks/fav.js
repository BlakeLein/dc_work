// API KEYS
const weatherAPI = "";
const npsAPI = "";

// HTML Grabs
const mainContainer = document.getElementById("main-container");
const select = document.getElementById("select");
const displayZone = document.getElementById("display-zone");
const titleZone = document.getElementById("title-zone");

const data = {
  method: "GET", // *GET, POST, PUT, DELETE, etc.
  cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
  credentials: "same-origin", // include, *same-origin, omit
  headers: {
    "Content-Type": "application/json",
    "x-api-key": npsAPI,
    Accept: "application/json",
    // 'Content-Type': 'application/x-www-form-urlencoded',
  },
  redirect: "follow", // manual, *follow, error
  referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
};

// Collapsable NavBar Fucntions
function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("menu-button").style.marginLeft = "250px";
}
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("menu-button").style.marginLeft = "0";
}

// Fucntions to open/close modal
const openModal = (modal) => {
  // if (modal == null) return;
  modal.classList.add("active");
  overlay.classList.add("active");
};
const closeModal = (modal) => {
  // if (modal == null) return;
  modal.classList.remove("active");
  overlay.classList.remove("active");
};

// Modal Grabs
const closeModalButton = document.getElementById("close-modal");
const overlay = document.getElementById("overlay");
const parkTitle = document.getElementById("header-title");
const modalBody = document.getElementById("modal-body");
const contactURL = document.getElementById("contact-url");
const address = document.getElementById("address");
const email = document.getElementById("email");
const phone = document.getElementById("phone");
const directions = document.getElementById("directions");
const monday = document.getElementById("monday");
const tuesday = document.getElementById("tuesday");
const wednesday = document.getElementById("wednesday");
const thursday = document.getElementById("thursday");
const friday = document.getElementById("friday");
const saturday = document.getElementById("saturday");
const sunday = document.getElementById("sunday");
const pictures = document.getElementById("pictures");
const activities = document.getElementById("activities");
const admission = document.getElementById("entry-fee");
const weatherBox = document.getElementById("weather");

// Puts park-specific info into the modal
const updateModalInfo = (parkObject) => {
  parkTitle.innerText = parkObject.fullName;
  contactURL.href = parkObject.url;
  getAddress(parkObject);
  getEmail(parkObject);
  getPhone(parkObject);
  directions.href = parkObject.directionsUrl;
  getHours(parkObject);
  getActivities(parkObject);
  getAdmission(parkObject);
  getImages(parkObject);
  getWeather(parkObject);
};

// Modal info functions
const getAddress = (parkObject) => {
  if (parkObject.addresses[0].line1 == "") {
    address.innerText = `${parkObject.addresses[0].line2}, ${parkObject.addresses[0].city}, ${parkObject.addresses[0].stateCode} ${parkObject.addresses[0].postalCode}`;
  } else if (parkObject.addresses[0].line2 == "") {
    address.innerText = `${parkObject.addresses[0].line1}, ${parkObject.addresses[0].city}, ${parkObject.addresses[0].stateCode} ${parkObject.addresses[0].postalCode}`;
  } else {
    address.innerText = `${parkObject.addresses[0].line1}, ${parkObject.addresses[0].line2}, ${parkObject.addresses[0].city}, ${parkObject.addresses[0].stateCode} ${parkObject.addresses[0].postalCode}`;
  }
};

const getEmail = (parkObject) => {
  if (parkObject.contacts.emailAddresses[0].emailAddress == undefined) {
    email.innerText = "None listed";
  } else if (parkObject.contacts.emailAddresses.length == 0) {
    phone.innerText = "None listed";
  } else {
    email.innerText = `Email: ${parkObject.contacts.emailAddresses[0].emailAddress}`;
  }
};

const getPhone = (parkObject) => {
  if (parkObject.contacts.phoneNumbers[0].phoneNumber == undefined) {
    phone.innerText = "None listed";
  } else if (parkObject.contacts.phoneNumbers.length == 0) {
    phone.innerText = "None listed";
  } else {
    phone.innerText = `Phone: ${parkObject.contacts.phoneNumbers[0].phoneNumber}`;
  }
};

const getHours = (parkObject) => {
  if (parkObject.operatingHours.length == 0) {
    let hoursZone = document.getElementById("hours");
    hoursZone.innerHTML = null;
    hoursZone.classList = "hours";
    hoursZone.innerText = "No Hours to show";
  } else {
    let weekDay = parkObject.operatingHours[0].standardHours;
    if (weekDay.monday == undefined) {
      monday.innerText = "Not defined for this day.";
    } else {
      monday.innerText = `${weekDay.monday}`;
    }
    if (weekDay.tuesday == undefined) {
      tuesday.innerText = "Not defined for this day.";
    } else {
      tuesday.innerText = `${weekDay.tuesday}`;
    }
    if (weekDay.wednesday == undefined) {
      wednesday.innerText = "Not defined for this day.";
    } else {
      wednesday.innerText = `${weekDay.wednesday}`;
    }
    if (weekDay.thursday == undefined) {
      thursday.innerText = "Not defined for this day.";
    } else {
      thursday.innerText = `${weekDay.thursday}`;
    }
    if (weekDay.friday == undefined) {
      friday.innerText = "Not defined for this day.";
    } else {
      friday.innerText = `${weekDay.friday}`;
    }
    if (weekDay.saturday == undefined) {
      saturday.innerText = "Not defined for this day.";
    } else {
      saturday.innerText = `${weekDay.saturday}`;
    }
    if (weekDay.sunday == undefined) {
      sunday.innerText = "Not defined for this day.";
    } else {
      sunday.innerText = `${weekDay.sunday}`;
    }
  }
};

const getActivities = (parkObject) => {
  if (parkObject.activities == undefined) {
    return "No activities to display";
  } else {
    for (let i = 0; i < parkObject.activities.length; i++) {
      let newItem = document.createElement("li");
      newItem.innerText = parkObject.activities[i].name;
      activities.append(newItem);
    }
  }
};

const getImages = (parkObject) => {
  if (parkObject.images.length == 0) {
    let message = document.createElement("h3");
    message.innerText = "No pictures to display.";
    message.classList = "small-title";
    pictures.append(message);
  } else {
    for (let i = 0; i < parkObject.images.length; i++) {
      let newImage = document.createElement("img");
      newImage.classList.add("modal-img");
      newImage.src = parkObject.images[i].url;
      pictures.append(newImage);
    }
  }
};

const getAdmission = (parkObject) => {
  if (parkObject.entranceFees.length === 0) {
    admission.innerText = "None Listed";
  } else if (parkObject.entranceFees[0].cost === undefined) {
    admission.innerText = "None Listed";
  } else if (parkObject.entranceFees[0].cost === "0.00") {
    admission.innerText = parkObject.entranceFees[0].description;
  } else {
    admission.innerText = `$${parkObject.entranceFees[0].cost}`;
    admission.classList.add("admission-style");
  }
};

// Weather Functions
const getWeather = async (parkObject) => {
  let lat = parkObject.latitude;
  let lon = parkObject.longitude;
  const weatherURL = `https://api.openweathermap.org/data/2.5/weather?units=imperial&lat=${lat}&lon=${lon}&appid=${weatherAPI}`;
  const weatherData = await fetch(weatherURL);
  const json = await weatherData.json();
  getWeatherIcon(json);
  getCurrentTemperature(json);
  getHighLow(json);
  getFeelsLike(json);
  getHumidity(json);
  getWindSpeed(json);
};

const getWeatherIcon = (object) => {
  let weatherZone = document.getElementById("icon");
  weatherZone.innerHTML = null;
  weatherIcon = document.createElement("img");
  weatherIcon.src = `http://openweathermap.org/img/wn/${object.weather[0].icon}@2x.png`;
  weatherZone.append(weatherIcon);
};

const getCurrentTemperature = (object) => {
  let currentTemperature = document.getElementById("ct-value");
  currentTemperature.innerText = `${object.main.temp.toFixed(0)}°`;
};

const getHighLow = (object) => {
  let highLow = document.getElementById("hl-value");
  highLow.innerText = `${object.main.temp_min.toFixed(
    0
  )}° / ${object.main.temp_max.toFixed(0)}°`;
};

const getFeelsLike = (object) => {
  let feelsLike = document.getElementById("fl-value");
  feelsLike.innerText = `${object.main.feels_like.toFixed(0)}°`;
};

const getHumidity = (object) => {
  let humidity = document.getElementById("h-value");
  humidity.innerText = `${object.main.humidity.toFixed(0)}%`;
};

const getWindSpeed = (object) => {
  let windSpeed = document.getElementById("ws-value");
  windSpeed.innerText = `${object.wind.speed.toFixed(1)} mph`;
};

// Allows the modal to close and overlay to disable when you click outside
overlay.addEventListener("click", () => {
  modal.classList.remove("active");
  overlay.classList.remove("active");
});

// Creates and appends the small state info cards to the page
const getParkCard = (parkObject) => {
  const parkCard = document.createElement("div");
  parkCard.classList = "state-card";
  let cardImage = document.createElement("img");
  cardImage.src = parkObject.images[0].url;
  let nameInfo = document.createElement("div");
  nameInfo.classList = "name-info";
  let cardTitle = document.createElement("h4");
  cardTitle.classList = "card-title";
  cardTitle.innerText = parkObject.fullName;
  let learnMore = document.createElement("button");
  learnMore.innerText = "Click to Learn More";
  learnMore.classList = "card-btn";
  let unfavorite = document.createElement("button");
  unfavorite.innerText = "Remove from Favorites";
  unfavorite.classList = "card-btn";
  nameInfo.append(cardTitle, learnMore, unfavorite);
  parkCard.append(cardImage, nameInfo);
  displayZone.append(parkCard);
  learnMore.addEventListener("click", () => {
    const modal = document.getElementById("modal");
    openModal(modal);
    updateModalInfo(parkObject);
  });
  unfavorite.addEventListener("click", () => {
    removePark(parkObject);
  });
};

const removePark = (parkObject) => {
  if (parkObject.fullName in localStorage) {
    localStorage.removeItem(`${parkObject.fullName}`);
  }
  unPackFavorites();
};

// Closes the modal after it's opened
closeModalButton.addEventListener("click", () => {
  const modal = document.getElementById("modal");
  closeModal(modal);
});

const unPackFavorites = () => {
  displayZone.innerHTML = null;
  let experiment = Object.keys(localStorage);
  for (let i = 0; i < experiment.length; i++) {
    let parkObjectDeserialized = JSON.parse(
      localStorage.getItem(experiment[i])
    );
    getParkCard(parkObjectDeserialized);
  }
};

unPackFavorites();
