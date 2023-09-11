#!/usr/bin/python3

"""this defines a class and inherited class-checking function"""
def is_kind_of_class(obj, a_class):	
	"""this returns True if the object is an instance of, or if 		the objectis an instance of a class that inherited from,		the specifie	 class ; otherwise False			"""
	if isinstance(obj, a_class):
		return True
	return False
