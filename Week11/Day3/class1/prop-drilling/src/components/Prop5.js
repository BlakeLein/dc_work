import React from "react";

export default function Prop5(props) {
  console.log(props.houses);
  return (
    <div>
      <h1>Prop5</h1>
      {props.houses.map((house) => {
        <h3>{house.name}</h3>;
      })}
    </div>
  );
}
