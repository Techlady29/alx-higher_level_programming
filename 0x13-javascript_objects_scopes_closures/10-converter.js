#!/usr/bin/node
export.converter = function (base) {
	return function (dec) {
		return dec.toString(base);
	};
};
