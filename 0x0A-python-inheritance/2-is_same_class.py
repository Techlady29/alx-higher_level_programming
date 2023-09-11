#!/usr/bin/python3

"""this Defines a class-checking function"""
def is_same_class(obj, a_class):
	"""returns True if the object is exactly an instance"""
	if type(obj) == a_class:
		return True
	return False
