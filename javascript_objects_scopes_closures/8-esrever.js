#!/usr/bin/node
exports.esrever = function (list) {
	let reversedlist = [];
	for (i = list.length - 1; i >= 0; i--) {
		reversedlist.push(list[i]);
	}
	return reversedlist;
}
