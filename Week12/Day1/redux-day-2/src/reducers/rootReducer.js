const initialState = {
  user: "Blake",
  weather: [],
  location: "",
  greeting: "Good morning",
};

const rootReducer = (state = initialState, action) => {
  switch (action.type) {
    case "GET_USER":
      console.log("hi I'm get user");
      // When you grab data from redux, you don't have to pass all of state, just what it needs
      return { ...state };
    case "SET_LOCATION":
      return { ...state, location: action.payload };
      // What returns when there is no action to match the dispatch
      return { ...state, location: action.payload };
    // What returns when there is no action to match the dispatch
    case "SET_WEATHER":
      console.log(state.weather.length);
      if (state.weather.length <= 4) {
        return { ...state, weather: [action.payload, ...state.weather] };
      } else {
        state.weather.pop();
        return { ...state, weather: [action.payload, ...state.weather] };
      }
    case "DELETE_CITY":
      const deleteCity = state.weather.filter(
        (weather) => !weather.name.includes(action.payload)
      );
      return { ...state, weather: deleteCity };

    default:
      return state;
  }
};

export default rootReducer;
