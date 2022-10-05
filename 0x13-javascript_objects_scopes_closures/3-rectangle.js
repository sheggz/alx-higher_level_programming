#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const arr = [];
    for (let i = 0; i < this.width; i++) { arr.push('X'); }
    for (let i = 0; i < this.height; i++) { console.log(arr.join('')); }
  }
}
module.exports = Rectangle;
