#!/usr/bin/node
// Require the Rectangle class from 4-rectangle.js file
const Rectangle = require('./4-rectangle');

// Define the Square class that inherits from Rectangle class.
class Square extends Rectangle {
  // class cosntructor
  constructor (size) {
  // call the super class cosntructor
    super(size, size);
  }
}
// Make the Square class visible
module.exports = Square;
