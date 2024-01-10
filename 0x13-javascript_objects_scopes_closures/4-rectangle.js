#!/usr/bin/node

// Define the Rectangle class
class Rectangle {
  // Constructor taking 2 args
  constructor (w, h) {
    // Initialize instance attribute w & h
    this.width = w;
    this.height = h;

    // check if w or h == 0 or not a +ve int
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      // create an empty object
      this.width = undefined;
      this.height = undefined;
    }
  }

  // Instance method to print the Rectangle using the X character
  print () {
    if (this.width !== undefined && this.height !== undefined) {
      for (let x = 0; x < this.height; x++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  // Instance method rotating the rectangle's width and height
  rotate () {
    if (this.width !== undefined && this.height !== undefined) {
      const tmp = this.width;
      this.width = this.height;
      this.height = tmp;
    }
  }

  // Instance method to multiply the rectangle's width & height
  double () {
    if (this.width !== undefined && this.height !== undefined) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

// Make the Rectangle class visible
module.exports = Rectangle;
