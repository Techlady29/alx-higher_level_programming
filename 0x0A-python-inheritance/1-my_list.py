#!/usr/bin/python3

"""this defines an inherited list class MyList."""
class MyList(list):
	"""inherits from list"""
	def print_sorted(self): 
		"""this prints the list in sorted ascending order"""
		print(sorted(self))
