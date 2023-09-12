#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
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
