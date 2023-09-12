#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let size = '';
      for (let i = 0; i < this.width; i++) {
        size += c;
      }
      console.log(size);
    }
  }
};
