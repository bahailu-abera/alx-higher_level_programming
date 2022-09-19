#!/usr/bin/node

exports.logMe = function (item) {
  this.numPrinted = 0;
  console.log(`${this.numPrinted}: ${item}`);
  this.numPrinted += 1;
};
