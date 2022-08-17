import React from "react";
import Prop2 from "./Prop2";

export default function Prop1(props) {
  return (
    <div>
      <h1>Prop1</h1>
      {props.children}
      <Prop2 houses={props.houses} owner={props.owner} />
    </div>
  );
}
