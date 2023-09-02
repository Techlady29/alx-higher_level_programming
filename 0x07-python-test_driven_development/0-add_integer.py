#!/usr/bin/python3

"""Modules has a function that adds 2 integers."""

def add_integer(a, b=98):
    """Return the addition of two numbers."""
    if type(a) not int and type(a) not float:
        raise TypeError("a must be an integer")
    if type(b) not int and type(b) not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
