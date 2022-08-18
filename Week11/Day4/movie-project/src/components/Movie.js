import React from "react";

export default function Movie(props) {
  console.log(props.data);
  return (
    <div>
      <h1>{props.data.Title}</h1>
      <img
        alt="poster"
        src={props.data.Poster == "N/A" ? "no-image.png" : props.data.Poster}
      />
      <h4>Released {props.data.Released}</h4>
      <h4>Directed by {props.data.Director}</h4>
      <h4>{props.data.Genre}</h4>
      <p>{props.data.Plot}</p>
    </div>
  );
}
