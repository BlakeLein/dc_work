import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { useAppSelector, useAppDispatch } from "./App/hooks";
import Product from "./components/Product";
import Cart from "./components/Cart";
import Homepage from "./components/Homepage";

function App(): JSX.Element {
  return (
    <div className="App">
      <Homepage />
    </div>
  );
}

export default App;
