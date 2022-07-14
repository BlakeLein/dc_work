console.log("Hi");

const showPokemon = async () => {
  const url = `https://pokeapi.co/api/v2/pokemon/`;
  const pokeData = await fetch(url);
  const json = await pokeData.json();
  console.log(json);
  console.log(json.next);
};

showPokemon();
