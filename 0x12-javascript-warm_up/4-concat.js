#!/usr/bin/node
const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (arg1 !== undefined && arg2 !== undefined) {
  console.log(`${arg1} is ${arg2}`);
} else {
  console.log("Usage: ./script.js <arg1> <arg2>");
}

