#!/usr/bin/node

const i = parseInt(process.argv[2]);
const arr = [];
if (!i) {
  console.log('Missing size');
} else {
  for (let k = 0; k < i; k++) {
    arr.push('X');
  }
  for (let k = 0; k < i; k++) {
    console.log(arr.join(''));
  }
}
