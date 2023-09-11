#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    let size = '';
    for (let i = 0; i < Number(process.argv[2]); i++) {
      size += 'X';
    }
    console.log(size);
  }
}
