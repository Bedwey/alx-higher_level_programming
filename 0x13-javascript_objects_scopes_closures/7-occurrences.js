#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let len = 0;
  for (let i = 0; i <= list.length; i++) {
    if (list[i] === searchElement) {
      len++;
    }
  }
  return len;
};
