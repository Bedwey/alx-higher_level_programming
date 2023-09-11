#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

if (isNaN(process.argv[2]) && isNaN(process.argv[3])) {
  console.log('NaN');
} else {
  console.log(add(Number(process.argv[2]), Number(process.argv[3])));
}
