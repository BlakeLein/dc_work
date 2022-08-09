import logo from "./logo.svg";
import "./App.css";
import Student from "./student";

function App() {
  const name = "Blake Lein";
  const students = [
    "Joe",
    "Jason",
    "Andrea",
    "Stacy",
    "West",
    "Ethan",
    "Amanda",
    "Rahmin",
    "Carlos",
    "Olivia",
  ];
  return (
    <div className="App">
      <h1>{name}</h1>
      {students.map((student) => (
        <>
          <Student student={student} />
        </>
      ))}
    </div>
  );
}

export default App;
