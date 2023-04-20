#!/usr/bin/node
function add (a = 3, b = 5) {
	return parseInt(a) + parseInt(b);
}

console.log(add(process.argv[2], process.argv[3]))
