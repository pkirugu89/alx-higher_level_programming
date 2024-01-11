#!/usr/bin/node
// Require the Square class from 5-square.js file
const Square5 = require('./5-square');

// Define the Square class that inherits from Rectangle class.
class Square extends Square5 {
  // Instance method for printing the square using character 'c'
  charPrint (c) {
  // If c is undefined, use character 'X'
    if (c === undefined) {
      c = 'X';
    }

    // Loop the square print using char 'c'
    for (let x = 0; x < this.height; x++) {
      console.log(c.repeat(this.width));
    }
  }
}

// Make the Square class visible
module.exports = Square;
