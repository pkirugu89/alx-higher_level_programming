#!/usr/bin/node
// Extracting the 1st argument
const argz = process.argv[2];
// Converting the arguments to an integer
const intVal = parseInt(argz);

// Check if the conversion is successful
if (!isNaN(intVal)) {
  console.log(`My number: ${intVal}`);
} else {
  console.log('Not a number');
}
