#!/usr/bin/node

const fs = require('fs');

// Get file paths from command-line arguments
const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const destinationPath = process.argv[4];

// Read the content of file A
fs.readFile(fileAPath, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    return;
  }

  // Read the content of file B
  fs.readFile(fileBPath, 'utf8', (err, dataB) => {
    if (err) {
      console.error(err);
      return;
    }

    // Concatenate the content of file A and file B
    const concatenatedContent = `${dataA}${dataB}`;

    // Write the concatenated content to the destination file
    fs.writeFile(destinationPath, concatenatedContent, (err) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(`Concatenated files saved to ${destinationPath}`);
    });
  });
});
