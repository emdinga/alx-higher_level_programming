#!/usr/bin/node
const fs = require('fs');
const path = require('path');
if (process.argv.length !== 5) {
  console.error('Usage: node concat-files.js <source-file-1> <source-file-2> <destination-file>');
  process.exit(1);
}
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${sourceFile1}: ${err.message}`);
    process.exit(1);
  }
  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${sourceFile2}: ${err.message}`);
      process.exit(1);
    }
    const concatenatedData = data1 + data2;
    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${destinationFile}: ${err.message}`);
        process.exit(1);
      }
      console.log(`Concatenation completed. Result written to ${destinationFile}`);
    });
  });
});

