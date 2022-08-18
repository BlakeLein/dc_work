import React from "react";
import MovieCard from "./MovieCard";
import "../App.css";

export default function MovieContainer(props) {
  return (
    <div>
      <h3>Results</h3>
      {props.data?.map((movie) => (
        <MovieCard key={movie.imdbID} data={movie} />
      ))}
    </div>
  );
}
