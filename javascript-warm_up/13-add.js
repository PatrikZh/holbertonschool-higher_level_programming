#!/usr/bin/node
function add (a, b) {
	a = parseInt(a) || 3;
	b = parseInt(b) || 5;
	return a + b;
}

console.log(add(process.argv[2], process.argv[3]))
