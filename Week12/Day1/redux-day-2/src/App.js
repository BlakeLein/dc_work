import "./App.css";
import { useSelector, useDispatch } from "react-redux";
import { useState } from "react";
import Weathercard from "./components/Weathercard";

function App() {
  const [inputValue, setInputValue] = useState("");
  const dispatch = useDispatch();
  const weather = useSelector((state) => state.weather);
  const location = useSelector((state) => state.location);
  const url = `https://api.openweathermap.org/data/2.5/weather?units=imperial&q=${location}&appid=${process.env.REACT_APP_WEATHER_KEY}`;

  const getWeather = async () => {
    const weather = await fetch(url);
    const json = await weather.json();
    console.log(json);
    dispatch({ type: "SET_WEATHER", payload: json });
  };

  return (
    <div className="App">
      <h1>Weather App</h1>
      <h1>{weather.conditions}</h1>
      <form
        className="form"
        onSubmit={(e) => {
          e.preventDefault();
          getWeather();
          setInputValue("");
        }}
      >
        <input
          value={inputValue}
          placeholder="Search by name or zip code"
          className="input"
          onChange={(e) => {
            setInputValue(e.target.value);
            dispatch({ type: "SET_LOCATION", payload: e.target.value });
          }}
        ></input>
        <input
          type="submit"
          className="search-btn"
          disabled={!location ? true : false}
        />
      </form>
      <div className="card-container">
        {weather?.map((weather) => (
          <Weathercard weather={weather} />
        ))}
      </div>
    </div>
  );
}

export default App;
