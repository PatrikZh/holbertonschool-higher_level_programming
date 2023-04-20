#!/usr/bin/node
function add (a, b) {
  const args = process.argv.slice(2);
  if (!a) {
    a = args[0] || 3;
  } 
  if (!b) {
    b = args[1] || 5;
  }
  return parseInt(a) + parseInt(b);
}

console.log(add());
