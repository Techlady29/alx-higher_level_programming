i#!/usr/bin/python3

"""Modules has a function that adds 2 integers."""

def add_integer(a, b=98):
    """Return the addition of two numbers."""
	if type(a) not in [int, float]:
		raise TypeError("a must be an integer")
	if type(b) not in [int, float]:	
		raise TypeError("b must be an integer")
	return int(a) + int(b)
