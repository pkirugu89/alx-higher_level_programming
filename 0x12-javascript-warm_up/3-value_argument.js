#!/usr/bin/node
// check if an argument is provided.
const firstArg = process.argv[2];

// printing the messages
if (typeof firstArg === 'undefined') {
  console.log('No Argument');
} else {
  console.log(firstArg);
}
