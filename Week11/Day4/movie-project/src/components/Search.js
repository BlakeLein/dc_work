import React from "react";
import MovieCard from "./MovieCard.js";

export default function Search(props) {
  return (
    <div className="search-bar">
      <h1>Find a Movie</h1>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          props.getMovies();
          props.changeInputText("");
        }}
      >
        <input
          type="text"
          value={props.inputText}
          onChange={(e) => {
            props.changeInputText(e.target.value);
          }}
          placeholder="Search Movies By Name"
        />
        <input type="radio" name="option" value="all" />
        <label>All</label>
        <input type="radio" name="option" value="movie" />
        <label>Movies</label>
        <input type="radio" name="option" value="series" />
        <label>TV Shows</label>
        <input type="radio" name="option" value="game" />
        <label>Video Games</label>
        <button type="submit">Search</button>
      </form>
      {props.data?.map((movie) => (
        <MovieCard
          key={movie.imdbID}
          updateSpecificData={props.updateSpecificData}
          data={movie}
        />
      ))}
    </div>
  );
}
