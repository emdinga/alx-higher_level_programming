#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  console.log(data);
});
