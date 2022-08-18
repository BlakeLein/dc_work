import "./App.css";
import Search from "./components/Search";
import About from "./components/About";
import Navbar from "./components/Navbar";
import Movie from "./components/Movie";
import MovieCard from "./components/MovieCard";
import MovieContainer from "./components/MovieContainer";
import { useState, useEffect } from "react";
import { Routes, Route } from "react-router-dom";

function App() {
  const [inputText, changeInputText] = useState("");
  const [data, updateData] = useState([]);
  const [specificData, updateSpecificData] = useState({});

  const getMovies = async () => {
    const response = await fetch(
      `http://www.omdbapi.com/?s=${inputText}&apikey=${process.env.REACT_APP_API_KEY}`
    );
    const json = await response.json();
    updateData(() => json.Search);
  };
  return (
    <div className="App">
      <Routes>
        <Route
          path="/"
          element={
            <Search
              inputText={inputText}
              changeInputText={changeInputText}
              data={data}
              updateData={updateData}
              getMovies={getMovies}
              updateSpecificData={updateSpecificData}
            />
          }
        />
        {/* <Route path="/movie-container" element={<MovieContainer />} /> */}
        <Route path="/movie-info" element={<Movie data={specificData} />} />
      </Routes>
    </div>
  );
}

export default App;
