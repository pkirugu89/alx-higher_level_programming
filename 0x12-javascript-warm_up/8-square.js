#!/usr/bin/node
// First Argument
const argz = process.argv[2];
// Convert argz to int
const size = parseInt(argz);
// Check if the conversion is successful
if (!isNaN(size)) {
  // print a square using for loop
  for (let x = 0; x < size; x++) {
    let row = '';
    for (let y = 0; y < size; y++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
