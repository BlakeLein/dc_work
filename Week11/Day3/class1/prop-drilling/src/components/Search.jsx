import React from "react";

export default function Search(props) {
  return (
    <div>
      <input
        type="text"
        placeholder="Search by name"
        value={props.search}
        onChange={(e) => {
          props.setSearch(e.target.value);
        }}
      />
    </div>
  );
}
