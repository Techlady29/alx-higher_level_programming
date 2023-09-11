#!/usr/bin/python3

"""this defines a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
	"""this represents a square"""
	def __init__(self, size):
		"""this Initialize a new square.

	Args:
		size (int): The size of the new square.
	"""
	self.integer_validator("size", size)
	super().__init__(size, size)
	self.__size = size
