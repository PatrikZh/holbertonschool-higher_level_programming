#!/usr/bin/node
const args = process.argv.slice(2)

if (args == 0) {
	console.log('No argument');
} else if (process.argv[2]) {
	console.log(process.argv[2]);
}
