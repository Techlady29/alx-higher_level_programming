#!/usr/bin/python3
"""this defines an object attribute lookup function"""

def lookup(obj):
	"""this returns the list of available attributes"""
	return dir(obj)
