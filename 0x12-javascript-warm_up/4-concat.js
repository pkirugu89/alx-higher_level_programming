#!/usr/bin/node
// Check if both arguments have been provided.
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Printing the messages.
if (typeof arg1 === 'undefined' && typeof arg2 === 'undefined') {
  console.log('Provide two arguments');
} else if (typeof arg1 === 'undefined') {
  console.log(`${arg1} is ${arg2}`);
} else if (typeof arg2 === 'undefined') {
  console.log(`${arg1} is ${arg2}`);
} else {
  console.log(`${arg1} is ${arg2}`);
}
