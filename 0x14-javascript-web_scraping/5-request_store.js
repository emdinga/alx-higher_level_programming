#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <file-path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Request failed with status code: ${response.statusCode}`);
    process.exit(1);
  }

  fs.writeFile(filePath, body, 'utf-8', (writeError) => {
    if (writeError) {
      console.error(writeError);
      process.exit(1);
    }
    console.log(`Content from ${url} has been saved to ${filePath}`);
  });
});

