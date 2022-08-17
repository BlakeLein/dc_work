import React from "react";
import "../App.css";
import { useState } from "react";

export default function PokeCard(props) {
  const [front, setFront] = useState(true);
  return (
    <div className="card">
      <div className="title">
        <h1>{props.character.name.toUpperCase()}</h1>
      </div>
      <div className="info">
        <img
          onClick={() => setFront(!front)}
          src={
            front
              ? props?.character?.sprites?.front
              : props?.character?.sprites?.back
          }
          alt=""
        />
        <div>
          <div>No: {props?.character?.id}</div>
          <div>Base HP: {props?.character?.hp}</div>
          <button
            onClick={() => {
              props.setPokemon(
                props.pokemon.filter(
                  (character) => character !== props.character
                )
              );
            }}
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  );
}
