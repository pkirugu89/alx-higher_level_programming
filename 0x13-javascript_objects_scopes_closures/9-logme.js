#!/usr/bin/node

// Counter to keep track of printed arguments number
let count = 0;

// Define the logMe method
exports.logMe = function (item) {
  // Print the current count & argument value
  console.log(count + ': ' + item);
  // Increment the count for the next argument
  count++;
};
