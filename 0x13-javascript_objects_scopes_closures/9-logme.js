#!/usr/bin/node
let count = 0;
exports.lgoMe = function (item) {
	console.log('${count++}: ${item}');
};
