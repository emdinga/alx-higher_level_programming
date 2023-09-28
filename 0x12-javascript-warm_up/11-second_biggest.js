#!/usr/bin/node
function findSecondLargest(numbers) {
  if (numbers.length < 2) {
    return 0;
  }

  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (const number of numbers) {
    const n = parseInt(number);
    if (!isNaN(n)) {
      if (n > largest) {
        secondLargest = largest;
        largest = n;
      } else if (n > secondLargest && n < largest) {
        secondLargest = n;
      }
    }
  }

  return secondLargest;
}
const args = process.argv.slice(2);
const secondLargest = findSecondLargest(args);
console.log(secondLargest);
