#!/usr/bin/node
// Extract the 1st argument
const argz = process.argv[2];

// converting the argz to an int
const count = parseInt(argz);
// Check if the conversion is successful
if (!isNaN(count)) {
  // Loop for printing 'C is fun' x times
  for (let x = 0; x < count; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
