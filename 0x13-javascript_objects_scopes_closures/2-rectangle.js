#!/usr/bin/node

// Define the Rectangle class
class Rectangle {
  // Constructor taking 2 arguments w and h
  constructor (w, h) {
    // Initialize instance attributes width and height
    this.width = w;
    this.height = h;

    // Check if w or h is equal to 0 or not a positive integer
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      // Create an empty object
      this.initializeEmptyObj();
    }
  }

  // Method to initialize an empty object
  initializeEmptyObj () {
	  this.width = undefined;
	  this.height = undefined;
  }
}

// Make the Rectangle class visible
module.exports = Rectangle;
