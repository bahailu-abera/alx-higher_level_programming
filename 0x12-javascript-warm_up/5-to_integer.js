#!/usr/bin/node
const argv = process.argv;

arg = Number(argv[2]);
if (Number.isSafeInteger(arg)) {
    console.log(`My number: ${arg}`);
} else {
    console.log("Not a Number");
}
