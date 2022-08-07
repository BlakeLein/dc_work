// const date = "0001-01-01";

// const splitDate = date.split("-");
// const year = splitDate[0];
// const month = splitDate[1];
// const day = splitDate[2];
// const formattedDate = `${month}-${day}-${year}`;
// return formattedDate;

const getFormattedTime = (time) => {
  const splitTime = time.split(":");
  if (splitTime[0] > "12") {
    const newTime = splitTime[0] - 12;
    const formattedTime = `${newTime}:${splitTime[1]} PM`;
    return formattedTime;
  } else {
    const formattedTime = `${splitTime[0]}:${splitTime[1]} AM`;
    return formattedTime;
  }
};

console.log(getFormattedTime("15:00"));

console.log(getFormattedTime("21:00"));

console.log(getFormattedTime("1:00"));
