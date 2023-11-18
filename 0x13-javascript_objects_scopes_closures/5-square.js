#!/usr/bin/node
module.export = class square extends require('./4-rectangle') {
	constructor (size) {
		supe(size, size);
	}
};
