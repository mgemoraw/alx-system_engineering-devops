#!/usr/bin/nodejs
const fs = require('fs');

// Specifying the file path
const filePath = process.argv[2];

readFile = (filePath) => {
  // Read the content of the file asynchronously
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      // Handles errors, e.g., file not found
      console.error(`Error reading file: ${err.message}`);
    } else {
      // Read and pring the contents of the file
      console.log(data);
    }
  });
};
