#!/usr/bin/node

const arr = require('./100-data').list;
let map1 = arr.map((x, y) => x * y);
console.log(arr);
console.log(map1);
