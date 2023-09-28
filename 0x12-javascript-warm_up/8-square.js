#!/usr/bin/node
const arg = process.argv[2];
const size = parseInt(arg);
if (!isNaN(size)) {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      console.log('X'.repeat(size));
    }
  } else {
    console.log('Size must be a positive integer.');
  }
} else {
  console.log('Missing size');
}
