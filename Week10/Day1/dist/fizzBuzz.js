"use strict";
function fizzBuzz(num) {
    for (let i = 0; i < num; i++) {
        if (i % 3 && i % 5) {
            return "FizzBuzz";
        }
        else if (i % 3) {
            return "Fizz";
        }
        else if (i % 5) {
            return "Buzz";
        }
        else {
            return i;
        }
    }
    return "Idk";
}
