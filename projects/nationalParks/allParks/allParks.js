require("dotenv").config();

// API KEYS

const weatherAPI = "";
const npsAPI = "";

// HTML Grabs
const mainContainer = document.getElementById("main-container");
const button = document.getElementById("button");
const select = document.getElementById("select");
const displayZone = document.getElementById("display-zone");
const titleZone = document.getElementById("title-zone");

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

// Collapsable NavBar Fucntions
function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("menu-button").style.marginLeft = "250px";
}
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("menu-button").style.marginLeft = "0";
}

// Data object to pass into fetch function
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
// List and Objects of states to work with

// Closes the modal after it's opened
closeModalButton.addEventListener("click", () => {
  const modal = document.getElementById("modal");
  closeModal(modal);
});

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

const statesObjectName = {
  Alabama: "AL",
  Alaska: "AK",
  Arizona: "AZ",
  Arkansas: "AR",
  California: "CA",
  Colorado: "CO",
  Connecticut: "CT",
  Delaware: "DE",
  DistrictofColumbia: "DC",
  Florida: "FL",
  Georgia: "GA",
  Hawaii: "HI",
  Idaho: "ID",
  Illinois: "IL",
  Indiana: "IN",
  Iowa: "IA",
  Kansas: "KS",
  Kentucky: "KY",
  Louisiana: "LA",
  Maine: "ME",
  Maryland: "MD",
  Massachusetts: "MA",
  Michigan: "MI",
  Minnesota: "MN",
  Mississippi: "MS",
  Missouri: "MO",
  Montana: "MT",
  Nebraska: "NE",
  Nevada: "NV",
  NewHampshire: "NH",
  NewJersey: "NJ",
  NewMexico: "NM",
  NewYork: "NY",
  NorthCarolina: "NC",
  NorthDakota: "ND",
  Ohio: "OH",
  Oklahoma: "OK",
  Oregon: "OR",
  Pennsylvania: "PA",
  RhodeIsland: "RI",
  SouthCarolina: "SC",
  SouthDakota: "SD",
  Tennessee: "TN",
  Texas: "TX",
  Utah: "UT",
  Vermont: "VT",
  Virginia: "VA",
  Washington: "WA",
  WestVirginia: "WV",
  Wisconsin: "WI",
  Wyoming: "WY",
};
const statesArray = [
  "Alabama",
  "Alaska",
  "Arizona",
  "Arkansas",
  "California",
  "Colorado",
  "Connecticut",
  "Florida",
  "Georgia",
  "Hawaii",
  "Idaho",
  "Illinois",
  "Indiana",
  "Iowa",
  "Kansas",
  "Kentucky",
  "Louisiana",
  "Maine",
  "Maryland",
  "Massachusetts",
  "Michigan",
  "Minnesota",
  "Mississippi",
  "Missouri",
  "Montana",
  "Nebraska",
  "Nevada",
  "New Hampshire",
  "New Jersey",
  "New Mexico",
  "New York",
  "North Carolina",
  "North Dakota",
  "Ohio",
  "Oklahoma",
  "Oregon",
  "Pennsylvania",
  "Rhode Island",
  "South Carolina",
  "South Dakota",
  "Tennessee",
  "Texas",
  "Utah",
  "Vermont",
  "Virginia",
  "Washington",
  "West Virginia",
  "Wisconsin",
  "Wyoming",
];

// Creates the states and appends them to the drop-down menu
const getStatesSelect = () => {
  for (s in statesArray) {
    let option = document.createElement("option");
    option.innerText = statesArray[s];
    select.append(option);
  }
};

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
  let favoriteButton = document.createElement("button");
  if (parkObject.fullName in localStorage == true) {
    favoriteButton.innerText = "Favorited!";
    favoriteButton.disabled = true;
  } else {
    favoriteButton.innerText = "Add to Favorites";
  }
  favoriteButton.classList = "card-btn";
  nameInfo.append(cardTitle, learnMore, favoriteButton);
  parkCard.append(cardImage, nameInfo);
  displayZone.append(parkCard);
  learnMore.addEventListener("click", () => {
    const modal = document.getElementById("modal");
    openModal(modal);
    updateModalInfo(parkObject);
  });
  favoriteButton.addEventListener("click", () => {
    favoriteButton.innerText = "Favorited!";
    favoriteButton.disabled = true;
    addToFavorites(parkObject);
  });
};

const addToFavorites = (parkObject) => {
  let parkObjectSerialized = JSON.stringify(parkObject);
  localStorage.setItem(`${parkObject.fullName}`, parkObjectSerialized);
};

// Takes the selected state and puts the park for each state on the screen
const selectByState = async (state) => {
  // Clear data on page
  input.innerText = "";
  titleZone.innerHTML = null;
  displayZone.innerHTML = null;

  // Put selected state onto the screen
  let stateTitle = document.createElement("h1");
  stateTitle.innerText = `National Parks in ${state}`;
  stateTitle.classList = "title-zone";
  titleZone.append(stateTitle);

  // Pull Parks DataBase
  let url = "https://developer.nps.gov/api/v1/parks?limit=467";
  const response = await fetch(url, data);
  const json = await response.json();

  // Remove space from selected state
  state = state.replace(/\s/g, "");

  // Loop through data and add parks in selected state
  for (let i = 0; i < json.data.length; i++) {
    if (json.data[i].states.includes(statesObjectName[state])) {
      getParkCard(json.data[i]);
    }
  }
};

// Script for Auto-fill search

const input = document.getElementById("input");

input.addEventListener("keyup", async (e) => {
  let listOfNames = [
    "Abraham Lincoln Birthplace National Historical Park",
    "Acadia National Park",
    "Adams National Historical Park",
    "African American Civil War Memorial",
    "African Burial Ground National Monument",
    "Agate Fossil Beds National Monument",
    "Ala Kahakai National Historic Trail",
    "Alagnak Wild River",
    "Alaska Public Lands",
    "Alcatraz Island",
    "Aleutian Islands World War II National Historic Area",
    "Alibates Flint Quarries National Monument",
    "Allegheny Portage Railroad National Historic Site",
    "Amache National Historic Site",
    "American Memorial Park",
    "Amistad National Recreation Area",
    "Anacostia Park",
    "Andersonville National Historic Site",
    "Andrew Johnson National Historic Site",
    "Aniakchak National Monument & Preserve",
    "Antietam National Battlefield",
    "Apostle Islands National Lakeshore",
    "Appalachian National Scenic Trail",
    "Appomattox Court House National Historical Park",
    "Arches National Park",
    "Arkansas Post National Memorial",
    "Arlington House, The Robert E. Lee Memorial",
    "Assateague Island National Seashore",
    "Aztec Ruins National Monument",
    "Badlands National Park",
    "Baltimore-Washington Parkway",
    "Bandelier National Monument",
    "Belmont-Paul Women's Equality National Monument",
    "Bent's Old Fort National Historic Site",
    "Bering Land Bridge National Preserve",
    "Big Bend National Park",
    "Big Cypress National Preserve",
    "Big Hole National Battlefield",
    "Big South Fork National River & Recreation Area",
    "Big Thicket National Preserve",
    "Bighorn Canyon National Recreation Area",
    "Birmingham Civil Rights National Monument",
    "Biscayne National Park",
    "Black Canyon Of The Gunnison National Park",
    "Blackstone River Valley National Historical Park",
    "Blue Ridge Parkway",
    "Bluestone National Scenic River",
    "Booker T Washington National Monument",
    "Boston African American National Historic Site",
    "Boston Harbor Islands National Recreation Area",
    "Boston National Historical Park",
    "Brices Cross Roads National Battlefield Site",
    "Brown v. Board of Education National Historical Park",
    "Bryce Canyon National Park",
    "Buck Island Reef National Monument",
    "Buffalo National River",
    "Cabrillo National Monument",
    "California National Historic Trail",
    "Camp Nelson National Monument",
    "Canaveral National Seashore",
    "Cane River Creole National Historical Park",
    "Canyon de Chelly National Monument",
    "Canyonlands National Park",
    "Cape Cod National Seashore",
    "Cape Hatteras National Seashore",
    "Cape Henry Memorial Part of Colonial National Historical Park",
    "Cape Krusenstern National Monument",
    "Cape Lookout National Seashore",
    "Capitol Hill Parks",
    "Capitol Reef National Park",
    "Captain John Smith Chesapeake National Historic Trail",
    "Capulin Volcano National Monument",
    "Carl Sandburg Home National Historic Site",
    "Carlsbad Caverns National Park",
    "Carter G. Woodson Home National Historic Site",
    "Casa Grande Ruins National Monument",
    "Castillo de San Marcos National Monument",
    "Castle Clinton National Monument",
    "Castle Mountains National Monument",
    "Catoctin Mountain Park",
    "Cedar Breaks National Monument",
    "Cedar Creek & Belle Grove National Historical Park",
    "Chaco Culture National Historical Park",
    "Chamizal National Memorial",
    "Channel Islands National Park",
    "Charles Pinckney National Historic Site",
    "Charles Young Buffalo Soldiers National Monument",
    "Chattahoochee River National Recreation Area",
    "Chesapeake & Ohio Canal National Historical Park",
    "Chesapeake Bay",
    "Chickamauga & Chattanooga National Military Park",
    "Chickasaw National Recreation Area",
    "Chiricahua National Monument",
    "Christiansted National Historic Site",
    "City Of Rocks National Reserve",
    "Civil War Defenses of Washington",
    "Clara Barton National Historic Site",
    "Colonial National Historical Park",
    "Colorado National Monument",
    "Coltsville National Historical Park",
    "Congaree National Park",
    "Constitution Gardens",
    "Coronado National Memorial",
    "Cowpens National Battlefield",
    "Crater Lake National Park",
    "Craters Of The Moon National Monument & Preserve",
    "Cumberland Gap National Historical Park",
    "Cumberland Island National Seashore",
    "Curecanti National Recreation Area",
    "Cuyahoga Valley National Park",
    "César E. Chávez National Monument",
    "Dayton Aviation Heritage National Historical Park",
    "De Soto National Memorial",
    "Death Valley National Park",
    "Delaware Water Gap National Recreation Area",
    "Denali National Park & Preserve",
    "Devils Postpile National Monument",
    "Devils Tower National Monument",
    "Dinosaur National Monument",
    "Dry Tortugas National Park",
    "Dwight D. Eisenhower Memorial",
    "Ebey's Landing National Historical Reserve",
    "Edgar Allan Poe National Historic Site",
    "Effigy Mounds National Monument",
    "Eisenhower National Historic Site",
    "El Camino Real de Tierra Adentro National Historic Trail",
    "El Camino Real de los Tejas National Historic Trail",
    "El Malpais National Monument",
    "El Morro National Monument",
    "Eleanor Roosevelt National Historic Site",
    "Ellis Island Part of Statue of Liberty National Monument",
    "Eugene O'Neill National Historic Site",
    "Everglades National Park",
    "Federal Hall National Memorial",
    "Fire Island National Seashore",
    "First Ladies National Historic Site",
    "First State National Historical Park",
    "Flight 93 National Memorial",
    "Florissant Fossil Beds National Monument",
    "Ford's Theatre",
    "Fort Bowie National Historic Site",
    "Fort Davis National Historic Site",
    "Fort Donelson National Battlefield",
    "Fort Dupont Park",
    "Fort Foote Park",
    "Fort Frederica National Monument",
    "Fort Laramie National Historic Site",
    "Fort Larned National Historic Site",
    "Fort Matanzas National Monument",
    "Fort McHenry National Monument and Historic Shrine",
    "Fort Monroe National Monument",
    "Fort Necessity National Battlefield",
    "Fort Point National Historic Site",
    "Fort Pulaski National Monument",
    "Fort Raleigh National Historic Site",
    "Fort Scott National Historic Site",
    "Fort Smith National Historic Site",
    "Fort Stanwix National Monument",
    "Fort Sumter and Fort Moultrie National Historical Park",
    "Fort Union National Monument",
    "Fort Union Trading Post National Historic Site",
    "Fort Vancouver National Historic Site",
    "Fort Washington Park",
    "Fossil Butte National Monument",
    "Franklin Delano Roosevelt Memorial",
    "Frederick Douglass National Historic Site",
    "Frederick Law Olmsted National Historic Site",
    "Fredericksburg & Spotsylvania National Military Park",
    "Freedom Riders National Monument",
    "Friendship Hill National Historic Site",
    "Gates Of The Arctic National Park & Preserve",
    "Gateway Arch National Park",
    "Gateway National Recreation Area",
    "Gauley River National Recreation Area",
    "General Grant National Memorial",
    "George Rogers Clark National Historical Park",
    "George Washington Birthplace National Monument",
    "George Washington Carver National Monument",
    "George Washington Memorial Parkway",
    "Gettysburg National Military Park",
    "Gila Cliff Dwellings National Monument",
    "Glacier Bay National Park & Preserve",
    "Glacier National Park",
    "Glen Canyon National Recreation Area",
    "Glen Echo Park",
    "Gloria Dei Church National Historic Site",
    "Golden Gate National Recreation Area",
    "Golden Spike National Historical Park",
    "Governors Island National Monument",
    "Grand Canyon National Park",
    "Grand Canyon-Parashant National Monument",
    "Grand Portage National Monument",
    "Grand Teton National Park",
    "Grant-Kohrs Ranch National Historic Site",
    "Great Basin National Park",
    "Great Egg Harbor River",
    "Great Falls Park",
    "Great Sand Dunes National Park & Preserve",
    "Great Smoky Mountains National Park",
    "Green Springs",
    "Greenbelt Park",
    "Guadalupe Mountains National Park",
    "Guilford Courthouse National Military Park",
    "Gulf Islands National Seashore",
    "Hagerman Fossil Beds National Monument",
    "Haleakalā National Park",
    "Hamilton Grange National Memorial",
    "Hampton National Historic Site",
    "Harmony Hall",
    "Harpers Ferry National Historical Park",
    "Harriet Tubman National Historical Park",
    "Harriet Tubman Underground Railroad National Historical Park",
    "Harry S Truman National Historic Site",
    "Hawaiʻi Volcanoes National Park",
    "Herbert Hoover National Historic Site",
    "Historic Jamestowne Part of Colonial National Historical Park",
    "Home Of Franklin D Roosevelt National Historic Site",
    "Homestead National Historical Park",
    "Hono'uli'uli National Historic Site",
    "Hopewell Culture National Historical Park",
    "Hopewell Furnace National Historic Site",
    "Horseshoe Bend National Military Park",
    "Hot Springs National Park",
    "Hovenweep National Monument",
    "Hubbell Trading Post National Historic Site",
    "Ice Age Floods National Geologic Trail",
    "Ice Age National Scenic Trail",
    "Independence National Historical Park",
    "Indiana Dunes National Park",
    "Isle Royale National Park",
    "Iñupiat Heritage Center",
    "James A Garfield National Historic Site",
    "Jean Lafitte National Historical Park and Preserve",
    "Jewel Cave National Monument",
    "Jimmy Carter National Historical Park",
    "John Day Fossil Beds National Monument",
    "John Fitzgerald Kennedy National Historic Site",
    "John Muir National Historic Site",
    "Johnstown Flood National Memorial",
    "Joshua Tree National Park",
    "Juan Bautista de Anza National Historic Trail",
    "Kalaupapa National Historical Park",
    "Kaloko-Honokōhau National Historical Park",
    "Katahdin Woods and Waters National Monument",
    "Katmai National Park & Preserve",
    "Kenai Fjords National Park",
    "Kenilworth Park & Aquatic Gardens",
    "Kennesaw Mountain National Battlefield Park",
    "Keweenaw National Historical Park",
    "Kings Mountain National Military Park",
    "Klondike Gold Rush - Seattle Unit National Historical Park",
    "Klondike Gold Rush National Historical Park",
    "Knife River Indian Villages National Historic Site",
    "Kobuk Valley National Park",
    "Korean War Veterans Memorial",
    "LBJ Memorial Grove on the Potomac",
    "Lake Clark National Park & Preserve",
    "Lake Mead National Recreation Area",
    "Lake Meredith National Recreation Area",
    "Lake Roosevelt National Recreation Area",
    "Lassen Volcanic National Park",
    "Lava Beds National Monument",
    "Lewis & Clark National Historic Trail",
    "Lewis and Clark National Historical Park",
    "Lincoln Boyhood National Memorial",
    "Lincoln Home National Historic Site",
    "Lincoln Memorial",
    "Little Bighorn Battlefield National Monument",
    "Little River Canyon National Preserve",
    "Little Rock Central High School National Historic Site",
    "Longfellow House Washington's Headquarters National Historic Site",
    "Lowell National Historical Park",
    "Lower Delaware National Wild and Scenic River",
    "Lower East Side Tenement Museum National Historic Site",
    "Lyndon B Johnson National Historical Park",
    "Maggie L Walker National Historic Site",
    "Maine Acadian Culture",
    "Mammoth Cave National Park",
    "Manassas National Battlefield Park",
    "Manhattan Project National Historical Park",
    "Manzanar National Historic Site",
    "Marsh - Billings - Rockefeller National Historical Park",
    "Martin Luther King, Jr. Memorial",
    "Martin Luther King, Jr. National Historical Park",
    "Martin Van Buren National Historic Site",
    "Mary McLeod Bethune Council House National Historic Site",
    "Medgar and Myrlie Evers Home National Monument",
    "Mesa Verde National Park",
    "Mill Springs Battlefield National Monument",
    "Minidoka National Historic Site",
    "Minute Man National Historical Park",
    "Minuteman Missile National Historic Site",
    "Mississippi National River and Recreation Area",
    "Missouri National Recreational River",
    "Mojave National Preserve",
    "Monocacy National Battlefield",
    "Montezuma Castle National Monument",
    "Moores Creek National Battlefield",
    "Mormon Pioneer National Historic Trail",
    "Morristown National Historical Park",
    "Mount Rainier National Park",
    "Mount Rushmore National Memorial",
    "Muir Woods National Monument",
    "Natchez National Historical Park",
    "Natchez Trace National Scenic Trail",
    "Natchez Trace Parkway",
    "National Capital Parks-East",
    "National Mall and Memorial Parks",
    "National Park of American Samoa",
    "National Parks of New York Harbor",
    "Natural Bridges National Monument",
    "Navajo National Monument",
    "New Bedford Whaling National Historical Park",
    "New England National Scenic Trail",
    "New Jersey Pinelands National Reserve",
    "New Orleans Jazz National Historical Park",
    "New River Gorge National Park and Preserve",
    "Nez Perce National Historical Park",
    "Nicodemus National Historic Site",
    "Ninety Six National Historic Site",
    "Niobrara National Scenic River",
    "Noatak National Preserve",
    "North Cascades National Park",
    "North Country National Scenic Trail",
    "Obed Wild & Scenic River",
    "Ocmulgee Mounds National Historical Park",
    "Oklahoma City National Memorial",
    "Old Spanish National Historic Trail",
    "Olympic National Park",
    "Oregon Caves National Monument & Preserve",
    "Oregon National Historic Trail",
    "Organ Pipe Cactus National Monument",
    "Overmountain Victory National Historic Trail",
    "Oxon Cove Park & Oxon Hill Farm",
    "Ozark National Scenic Riverways",
    "Padre Island National Seashore",
    "Palo Alto Battlefield National Historical Park",
    "Paterson Great Falls National Historical Park",
    "Pea Ridge National Military Park",
    "Pearl Harbor National Memorial",
    "Pecos National Historical Park",
    "Pennsylvania Avenue",
    "Perry's Victory & International Peace Memorial",
    "Petersburg National Battlefield",
    "Petrified Forest National Park",
    "Petroglyph National Monument",
    "Pictured Rocks National Lakeshore",
    "Pinnacles National Park",
    "Pipe Spring National Monument",
    "Pipestone National Monument",
    "Piscataway Park",
    "Point Reyes National Seashore",
    "Pony Express National Historic Trail",
    "Port Chicago Naval Magazine National Memorial",
    "Potomac Heritage National Scenic Trail",
    "Poverty Point National Monument",
    "President William Jefferson Clinton Birthplace Home National Historic Site",
    "President's Park (White House)",
    "Presidio of San Francisco",
    "Prince William Forest Park",
    "Pullman National Monument",
    "Puʻuhonua o Hōnaunau National Historical Park",
    "Puʻukoholā Heiau National Historic Site",
    "Rainbow Bridge National Monument",
    "Reconstruction Era National Historical Park",
    "Redwood National and State Parks",
    "Richmond National Battlefield Park",
    "Rio Grande Wild & Scenic River",
    "River Raisin National Battlefield Park",
    "Rock Creek Park",
    "Rocky Mountain National Park",
    "Roger Williams National Memorial",
    "Roosevelt Campobello International Park",
    "Rosie the Riveter WWII Home Front National Historical Park",
    "Russell Cave National Monument",
    "Sagamore Hill National Historic Site",
    "Saguaro National Park",
    "Saint Croix Island International Historic Site",
    "Saint Croix National Scenic Riverway",
    "Saint Paul's Church National Historic Site",
    "Saint-Gaudens National Historical Park",
    "Salem Maritime National Historic Site",
    "Salinas Pueblo Missions National Monument",
    "Salt River Bay National Historical Park and Ecological Preserve",
    "San Antonio Missions National Historical Park",
    "San Francisco Maritime National Historical Park",
    "San Juan Island National Historical Park",
    "San Juan National Historic Site",
    "Sand Creek Massacre National Historic Site",
    "Santa Fe National Historic Trail",
    "Santa Monica Mountains National Recreation Area",
    "Saratoga National Historical Park",
    "Saugus Iron Works National Historic Site",
    "Scotts Bluff National Monument",
    "Selma To Montgomery National Historic Trail",
    "Sequoia & Kings Canyon National Parks",
    "Shenandoah National Park",
    "Shiloh National Military Park",
    "Sitka National Historical Park",
    "Sleeping Bear Dunes National Lakeshore",
    "Springfield Armory National Historic Site",
    "Star-Spangled Banner National Historic Trail",
    "Statue Of Liberty National Monument",
    "Ste. Geneviève National Historical Park",
    "Steamtown National Historic Site",
    "Stones River National Battlefield",
    "Stonewall National Monument",
    "Sunset Crater Volcano National Monument",
    "Tallgrass Prairie National Preserve",
    "Thaddeus Kosciuszko National Memorial",
    "Theodore Roosevelt Birthplace National Historic Site",
    "Theodore Roosevelt Inaugural National Historic Site",
    "Theodore Roosevelt Island",
    "Theodore Roosevelt National Park",
    "Thomas Cole National Historic Site",
    "Thomas Edison National Historical Park",
    "Thomas Jefferson Memorial",
    "Thomas Stone National Historic Site",
    "Timpanogos Cave National Monument",
    "Timucuan Ecological & Historic Preserve",
    "Tonto National Monument",
    "Touro Synagogue National Historic Site",
    "Trail Of Tears National Historic Trail",
    "Tule Lake National Monument",
    "Tule Springs Fossil Beds National Monument",
    "Tumacácori National Historical Park",
    "Tupelo National Battlefield",
    "Tuskegee Airmen National Historic Site",
    "Tuskegee Institute National Historic Site",
    "Tuzigoot National Monument",
    "Ulysses S Grant National Historic Site",
    "Upper Delaware Scenic & Recreational River",
    "Valles Caldera National Preserve",
    "Valley Forge National Historical Park",
    "Vanderbilt Mansion National Historic Site",
    "Vicksburg National Military Park",
    "Vietnam Veterans Memorial",
    "Virgin Islands Coral Reef National Monument",
    "Virgin Islands National Park",
    "Voyageurs National Park",
    "Waco Mammoth National Monument",
    "Walnut Canyon National Monument",
    "War In The Pacific National Historical Park",
    "Washington Monument",
    "Washington-Rochambeau Revolutionary Route National Historic Trail",
    "Washita Battlefield National Historic Site",
    "Weir Farm National Historical Park",
    "Whiskeytown National Recreation Area",
    "White Sands National Park",
    "Whitman Mission National Historic Site",
    "William Howard Taft National Historic Site",
    "Wilson's Creek National Battlefield",
    "Wind Cave National Park",
    "Wing Luke Museum Affiliated Area",
    "Wolf Trap National Park for the Performing Arts",
    "Women's Rights National Historical Park",
    "World War I Memorial",
    "World War II Memorial",
    "Wrangell - St Elias National Park & Preserve",
    "Wright Brothers National Memorial",
    "Wupatki National Monument",
    "Yellowstone National Park",
    "Yorktown Battlefield Part of Colonial National Historical Park",
    "Yosemite National Park",
    "Yucca House National Monument",
    "Yukon - Charley Rivers National Preserve",
    "Zion National Park",
  ];

  // Initially remove all elements (so if user erases a letter or adds a new letter - clean up previous outputs)
  removeElements();
  for (let i of listOfNames) {
    // Convert input to lower-case and compare
    if (
      i.toLowerCase().startsWith(input.value.toLowerCase()) &&
      input.value != ""
    ) {
      //Create list element
      let listItem = document.createElement("li");
      // One common class name
      listItem.classList.add("list-items");
      listItem.style.cursor = "pointer";
      listItem.setAttribute("onclick", "displayNames('" + i + "')");
      // Display matched part in bold
      let word = "<b>" + i.substr(0, input.value.length) + "</b>";
      word += i.substr(input.value.length);

      // Display the value in array
      listItem.innerHTML = word;
      document.querySelector(".list").appendChild(listItem);
    }
  }
});

const displayNames = (value) => {
  input.value = value;
  removeElements();
};

const removeElements = () => {
  // Clear all the items
  let items = document.querySelectorAll(".list-items");
  items.forEach((item) => {
    item.remove();
  });
};

const searchButton = document.getElementById("type-search");
searchButton.addEventListener("click", async () => {
  titleZone.innerHTML = null;
  displayZone.innerHTML = null;
  select.value = "";
  let url = "https://developer.nps.gov/api/v1/parks?limit=467";
  const response = await fetch(url, data);
  const json = await response.json();

  for (let i = 0; i < json.data.length; i++) {
    if (json.data[i].fullName == input.value) {
      getParkCard(json.data[i]);
    }
  }
});

// Run on screen load
getStatesSelect();

select.addEventListener("change", () => selectByState(select.value));
