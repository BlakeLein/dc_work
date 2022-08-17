import React from "react";
import Prop5 from "./Prop5";

export default function Prop4(props) {
  return (
    <div>
      <h1>Prop4</h1>
      <Prop5 houses={props.houses} owner={props.owner} />
    </div>
  );
}
