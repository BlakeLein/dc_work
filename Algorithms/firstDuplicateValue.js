// Brute force solution - O(n) time and O(n) space
const getFirstDuplicateValue = (array) => {
  let newArray = [];
  if (array.length <= 1 || array.length == undefined) {
    return -1;
  }
  for (let i = 0; i < array.length; i++) {
    if (newArray.includes(array[i])) {
      return array[i];
    } else if (!newArray.includes(array[i])) {
      newArray.push(array[i]);
    }
  }
  if (newArray.length === array.length) {
    return -1;
  }
};

// Solution using sets O(n) time, O(1) space
const getDuplicateWithSet = (array) => {
  const setArray = new Set();
  for (let i = 0; i < array.length; i++) {
    if (setArray.has(array[i])) {
      return array[i];
    } else {
      setArray.add(array[i]);
    }
  }
  return -1;
};

// Test cases
const testOne = [2, 1, 5, 2, 3, 3, 4];
const testTwo = [1, 1, 2, 3, 3, 2, 2];
const testThree = [];
const testFour = [3];
const testFive = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Test brute force
console.log(getFirstDuplicateValue(testThree));
console.log(getFirstDuplicateValue(testTwo));
console.log(getFirstDuplicateValue(testOne));
console.log(getFirstDuplicateValue(testFour));
console.log(getFirstDuplicateValue(testFive));

// Test set method
console.log(getDuplicateWithSet(testOne));
console.log(getDuplicateWithSet(testTwo));
console.log(getDuplicateWithSet(testThree));
console.log(getDuplicateWithSet(testFour));
console.log(getDuplicateWithSet(testFive));
