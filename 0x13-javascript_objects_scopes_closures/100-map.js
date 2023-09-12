#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const newList = [];
for (let i = 0; i < list.length; i++) {
  newList.push(list[i] * i);
}
console.log(newList);
