#!/usr/bin/node

function toBaseTen (num) {
  return num;
}

function toBaseTwo (num) {
  const binary = [];
  while (num > 0) {
    binary.push(num % 2);
    num = Math.floor(num / 2);
  }
  return binary.reverse().join('');
}

function toBaseSixteen (num) {
  const hexa = [];
  while (num > 0) {
    const mod = num % 16;
    switch (mod) {
      case 10:
        hexa.push('a');
        break;
      case 11:
        hexa.push('b');
        break;
      case 12:
        hexa.push('c');
        break;
      case 13:
        hexa.push('d');
        break;
      case 14:
        hexa.push('e');
        break;
      case 15:
        hexa.push('f');
        break;
      default:
        hexa.push(mod);
    }
    num = Math.floor(num / 16);
  }
  return hexa.reverse().join('');
}

exports.converter = function (base) {
  if (base === 2) {
    return toBaseTwo;
  } else if (base === 10) {
    return toBaseTen;
  } else if (base === 16) {
    return toBaseSixteen;
  }
};
