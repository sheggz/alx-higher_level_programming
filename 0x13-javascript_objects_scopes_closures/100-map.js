#!/usr/bin/node

const arr = require('./100-data').list;

let idx = 0;
const map1 = arr.map(x => x * idx++);
console.log(`${arr}\n${map1}`);
