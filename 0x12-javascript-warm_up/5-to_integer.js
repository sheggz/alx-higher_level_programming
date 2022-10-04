#!/usr/bin/node

let i = process.argv.splice(2);
i = parseInt(i[0]);
if (i) {
  console.log('My number: %d', i);
} else { console.log('Not a number'); }
