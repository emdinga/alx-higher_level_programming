#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file-path> <text-to-write>');
  process.exit(1);
}

const filePath = process.argv[2];
const textToWrite = process.argv[3];

fs.writeFile(filePath, textToWrite, 'utf-8', (error) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  console.log(`The text has been written to ${filePath}`);
});

