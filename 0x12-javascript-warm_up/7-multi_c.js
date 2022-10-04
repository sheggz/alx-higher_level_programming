#!/usr/bin/node

let i = process.argv[2];
i = parseInt(i);

if (!i) {
  console.log('Missing number of occurrences');
} else {
  while (i) {
    console.log('C is fun');
    i--;
  }
}
