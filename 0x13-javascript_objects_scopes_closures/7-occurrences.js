#!/usr/bin/node

// Define the nbOcurences method
exports.nbOccurences = function (list, searchElement) {
  // Use the filter method to count occurences
  const occurrences = list.filter(element => element === searchElement);
  // Return the occurrence's length
  return occurrences.length;
};
