import "./App.css";
import students from "./dummyData.js";
import { useState } from "react";
import Header from "./Header";
import SideMenu from "./SideMenu";
import AdMenu from "./AdMenus";
import Content from "./Content";
import Footer from "./Footer";
import Links from "./Links";

//hook
// to change state in functional components
function App() {
  // useState hook syntax (useState() is a function)
  // const [] = useState()
  // inside [] is 2 things: [stateVariable, functionToChangeTheStateVariable]
  // Variable is typically named "set" + variableName
  // 0 is the default value we are giving the variable "counter".
  // This default value can be an array or object or boolean too.

  // Any hook or function that changes the state must be in an anonymous function (see line 20 and 21)
  // const [counter, setCounter] = useState(0); // This is the hook
  // const [mood, setMood] = useState("happy");
  const [toDo, setToDo] = useState([]);
  const [toDoItem, setToDoItem] = useState("");
  const addToDo = () => {
    setToDo([...toDo, toDoItem]);
    setToDoItem = "";
  };

  const deleteToDo = () => {
    const filterToDoList = toDo.splice(index, 1);
  };

  return (
    <div className="App">
      <div class="top">
        <Header />
        <Links />
      </div>
      <div class="middle">
        <SideMenu />
        <Content />
        <AdMenu />
      </div>
      <Footer />
      {/* <h1>Counter: {counter}</h1>
      <button onClick={() => setCounter(() => counter + 1)}>+</button>
      <button onClick={() => setCounter(() => counter - 1)}>-</button>

      <h1>How are you feeling today?</h1>
      <h1>{mood ? "happy" : "sad"}</h1>
      <button onClick={() => setMood(!mood)}>Change Mood</button> */}
      <div>
        <h1>To Do List</h1>
        <h3>Add a To Do Item</h3>
        <input
          onChange={(e) => setToDoItem(e.target.value)}
          type="text"
        ></input>
        <button onClick={() => addToDo()}>Add Item</button>
        {toDo.map((todo, i) => (
          <>
            <p>
              {todo} {i}
            </p>
            <button onClick={() => deleteToDo(i)}>X</button>
          </>
        ))}
      </div>
    </div>
  );
}

export default App;
