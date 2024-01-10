#!/usr/bin/node
// Define add function
const add = (a, b) => {
  return a + b;
};

// 1st and 2nd arguments
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

// Check if the conversions are successful
if (!isNaN(arg1) && !isNaN(arg2)) {
  // call add() and print the results
  console.log(add(arg1, arg2));
} else {
  console.log('NaN');
}
