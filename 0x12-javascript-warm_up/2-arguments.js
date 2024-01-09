#!/usr/bin/node
// Checking the number of arguments
const msgArgs = process.argv.length - 2;

// Printing the corresponding messages
if (msgArgs === 0) {
  console.log('No argument');
} else if (msgArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
