import "../App.css";

import React from "react";
import { useSelector, useDispatch } from "react-redux";

export default function Weathercard(props) {
  const weather = useSelector((state) => state.weather);
  const dispatch = useDispatch();
  const ICON_URL = `http://openweathermap.org/img/wn/${props?.weather?.weather[0].icon}@2x.png`;
  const deleteCity = (name) => {
    dispatch({ type: "DELETE_CITY", payload: name });
  };

  return (
    <div className="weather-card">
      <div className="card-title">
        <h1>{props?.weather?.name}</h1>
        <button
          name={props?.weather?.name}
          onClick={
            (e) => {
              deleteCity(e.target.name);
            }

            // (e) => deleteCity(e.target.value)
          }
        >
          x
        </button>
      </div>
      <div className="card-info">
        <div className="container">
          <img src={ICON_URL} alt="weather-icon" />
          <p className="temp">{props?.weather?.main?.temp.toFixed(0)}°</p>
        </div>
        <div className="container-2">
          <div className="item">
            <p>Feels Like</p>
            <p>{props?.weather?.main?.feels_like.toFixed(0)}°</p>
          </div>
          <div className="item">
            <p>Humidity</p>
            <p>{props?.weather?.main?.humidity.toFixed(0)}%</p>
          </div>
          <div className="item">
            <p>Wind</p>
            <p>{props?.weather?.wind?.speed.toFixed(0)} mph</p>
          </div>
        </div>
      </div>
    </div>
  );
}

// const getSunRise = json => {
//     let date = new Date(json.sys.sunrise * 1000)
//     let hour = date.getHours().toString().padStart(2, 0)
//     let min = date.getMinutes().toString().padStart(2, 0)
//     let sunRise = `${hour}${min}`

// const getSunSet = json => {
//     let date = new Date(json.sys.sunset * 1000)
//     let hour = date.getHours().toString().padStart(2, 0)
//     let min = date.getMinutes().toString().padStart(2, 0)
//     let sunSet = `${hour}${min}`
