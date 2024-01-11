#!/usr/bin/node

// Define the esrever method
exports.esrever = function (list) {
  // Copy the original list to avoid direct modifications
  const reversedList = list.slice();

  // Use a loop to reverse the copied list's elements.
  for (let x = 0, y = reversedList.length - 1; x < y; x++, y--) {
    // swap elements at positions x and y.
    const temp = reversedList[x];
    reversedList[x] = reversedList[y];
    reversedList[y] = temp;
  }
  // Return the reversedList
  return reversedList;
};
