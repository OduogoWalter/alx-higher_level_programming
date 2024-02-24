#!/usr/bin/node

const { list } = require('./100-data');

// Create a new list using the map method
const newList = list.map((value, index) => value * index);

// Print the initial list
console.log(list);

// Print the new list
console.log(newList);
