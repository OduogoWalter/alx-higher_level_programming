#!/usr/bin/node

const { dict } = require('./101-data');

// Function to invert the dictionary
function invertDictionary(dictionary) {
  const invertedDict = {};

  // Loop through the original dictionary
  for (const key in dictionary) {
    const value = dictionary[key];

    // If the value is not a key in the inverted dictionary, create an empty array
    if (!invertedDict[value]) {
      invertedDict[value] = [];
    }

    // Push the key into the array corresponding to its value in the inverted dictionary
    invertedDict[value].push(key);
  }

  return invertedDict;
}

// Compute the new dictionary by inverting the original dictionary
const newDict = invertDictionary(dict);

// Print the new dictionary
console.log(newDict);
