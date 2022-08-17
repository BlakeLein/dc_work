import React from "react";
import Prop4 from "./Prop4";

export default function Prop3(props) {
  return (
    <div>
      <h1>Prop3</h1>
      <Prop4 houses={props.houses} owner={props.owner} />
    </div>
  );
}
