#!/usr/bin/node
const argv = process.argv;

let secondLargest = 0; let largest = argv[2];
for (let i = 3; i < argv.length; i++) {
  if (argv[i] > largest) {
    secondLargest = largest;
    largest = argv[i];
  } else if (argv[i] > secondLargest) {
    secondLargest = argv[i];
  }
}
console.log(secondLargest);
