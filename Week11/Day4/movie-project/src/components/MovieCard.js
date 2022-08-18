import React from "react";
import { Link } from "react-router-dom";
import "../App.css";

export default function MovieCard(props) {
  const getMovieDetails = async () => {
    const getData = await fetch(
      `http://www.omdbapi.com/?i=${props.data.imdbID}&apikey=${process.env.REACT_APP_API_KEY}&`
    );
    const json = await getData.json();
    props.updateSpecificData(json);
  };
  return (
    <div className="movie-card">
      <h2>{props?.data?.Title}</h2>

      <img
        alt="poster"
        src={props.data.Poster == "N/A" ? "no-image.png" : props.data.Poster}
      />
      <Link to="/movie-info">
        <button onClick={() => getMovieDetails()}>More Info</button>
      </Link>
    </div>
  );
}
