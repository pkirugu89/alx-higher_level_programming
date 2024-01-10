#!/usr/bin/node
// Extracting the arguments and converting them to integers
const intz = process.argv.slice(2).map(arg => parseInt(arg));

// Sorting the array of integers in descending order
const sortedIntz = intz.sort((a, b) => b - a);

// Finding the second biggest integer
const secondBiggest = sortedIntz[1] || 0;

// Printing the result
console.log(secondBiggest);
