// Class Photo

const classPhoto = (red, blue) => {
  red.sort(function (a, b) {
    return a - b;
  });
  blue.sort(function (a, b) {
    return a - b;
  });
  if (red[0] > blue[0]) {
    for (i = 0; i < red.length; i++) {
      if (red[i] <= blue[i]) {
        return false;
      } else {
        return true;
      }
    }
  } else {
    for (i = 0; i < blue.length; i++) {
      if (blue[i] <= red[i]) {
        return false;
      } else {
        return true;
      }
    }
  }
  return false;
};

let blue1 = [20, 5, 4, 4, 4, 4, 4, 4];
let red1 = [19, 19, 21, 1, 1, 1, 1, 1];

let blue2 = [5, 6, 7, 2, 3, 1, 2, 3];
let red2 = [1, 1, 1, 1, 1, 1, 1, 1];

// console.log(
//   red1.sort(function (a, b) {
//     return a - b;
//   })
// );
// console.log(
//   blue1.sort(function (a, b) {
//     return a - b;
//   })
// );

console.log(classPhoto(red1, blue1));
