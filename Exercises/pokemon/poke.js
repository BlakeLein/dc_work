const pokemon = document.getElementById("pokemon");
const cardContainer = document.querySelector(".pokemon-card");

const bulbasaur = pokemon.children[0];
const charizard = pokemon.children[1];
const pikachu = pokemon.children[2];
const blastoise = pokemon.children[3];
const garchomp = pokemon.children[4];

pokemon.onchange = (event) => showPokemon(event.target.value);

const showPokemon = (i) => {
  cardContainer.innerHTML = null;
  if (i === "bulbasaur") {
    let card = document.createElement("div");
    card.classList = "card";
    cardContainer.append(card);
    let name = document.createElement("h1");
    name.innerText = "It's Bulbasaur!";
    cardContainer.append(name);
    let picture = document.createElement("img");
    picture.src = "bulbasaur.png";
    card.append(picture);
    let stats = document.createElement("div");
    stats.classList = "stats";
    let pokeName = document.createElement("p");
    pokeName.classList = "name";
    pokeName.innerText = "Bulbasaur     No. 1";
    let info = document.createElement("p");
    info.innerText = `Seed Pokemon. Length: 2' 4", Weight: 15 lbs.`;
    stats.append(pokeName);
    stats.append(info);
    card.append(stats);
  }
  if (i === "charizard") {
    let card = document.createElement("div");
    card.classList = "card";
    cardContainer.append(card);
    let name = document.createElement("h1");
    name.innerText = "It's Charizard!";
    cardContainer.append(name);
    let picture = document.createElement("img");
    picture.src = "charizard.png";
    card.append(picture);
    let stats = document.createElement("div");
    stats.classList = "stats";
    let pokeName = document.createElement("p");
    pokeName.classList = "name";
    pokeName.innerText = "Charizard     No. 6";
    let info = document.createElement("p");
    info.innerText = `Flame Pokemon. Height: 5' 7", Weight: 199.5 lbs.`;
    stats.append(pokeName);
    stats.append(info);
    card.append(stats);
  }
  if (i === "pikachu") {
    let card = document.createElement("div");
    card.classList = "card";
    cardContainer.append(card);
    let name = document.createElement("h1");
    name.innerText = "It's Pikachu!";
    cardContainer.append(name);
    let picture = document.createElement("img");
    picture.src = "pika.png";
    card.append(picture);
    let stats = document.createElement("div");
    stats.classList = "stats";
    let pokeName = document.createElement("p");
    pokeName.classList = "name";
    pokeName.innerText = "Pikachu     No. 25";
    let info = document.createElement("p");
    info.innerText = `Mouse Pokemon. Length: 1' 4", Weight: 13 lbs.`;
    stats.append(pokeName);
    stats.append(info);
    card.append(stats);
  }
  if (i === "blastoise") {
    let card = document.createElement("div");
    card.classList = "card";
    cardContainer.append(card);
    let name = document.createElement("h1");
    name.innerText = "It's Blastoise!";
    cardContainer.append(name);
    let picture = document.createElement("img");
    picture.src = "blastoise.png";
    card.append(picture);
    let stats = document.createElement("div");
    stats.classList = "stats";
    let pokeName = document.createElement("p");
    pokeName.classList = "name";
    pokeName.innerText = "Blastoise     No. 9";
    let info = document.createElement("p");
    info.innerText = `Shellfish Pokemon. Length: 5' 3", Weight: 189 lbs.`;
    stats.append(pokeName);
    stats.append(info);
    card.append(stats);
  }
  if (i === "garchomp") {
    let card = document.createElement("div");
    card.classList = "card";
    cardContainer.append(card);
    let name = document.createElement("h1");
    name.innerText = "It's Garchomp!";
    cardContainer.append(name);
    let picture = document.createElement("img");
    picture.src = "garchomp.png";
    card.append(picture);
    let stats = document.createElement("div");
    stats.classList = "stats";
    let pokeName = document.createElement("p");
    pokeName.classList = "name";
    pokeName.innerText = "Garchomp     No. 445";
    let info = document.createElement("p");
    info.classList = "info";
    info.innerText = `Mach Pokemon. Length: 6' 3", Weight: 209 lbs.`;
    stats.append(pokeName);
    stats.append(info);
    card.append(stats);
  }
};
