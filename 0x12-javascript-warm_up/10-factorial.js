#!/usr/bin/node
// Define factorial()
const factorial = (n) => {
  if (isNaN(n)) {
    // Factorial of NaN is 1
    return 1;
  }
  if (n === 0 || n === 1) {
    // Base case: factorial of 0 & 1 is 1
    return 1;
  } else {
    return n * factorial(n - 1);
  }
};

// 1st argument
const argz = parseInt(process.argv[2]);
// Calling the factorial() and print the result
console.log(factorial(argz));
