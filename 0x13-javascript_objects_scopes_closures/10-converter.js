#!/usr/bin/node

// Define the converter function
exports.converter = function (base) {
  // Return a function that converts a number to a specified base
  return function (number) {
    // Use toString() to convert number to specified base
    return number.toString(base);
  };
};
