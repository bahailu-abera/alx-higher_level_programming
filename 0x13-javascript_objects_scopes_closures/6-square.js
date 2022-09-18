#!/usr/bin/node
const { Square: Square5 } = require('./5-square.js');

class Square extends Square5 {
  charPrint (value = 'X') {
    console.log(value);
  }
}
module.exports = Square;
