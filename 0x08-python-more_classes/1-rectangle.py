#!/usr/bin/python3
"""This defines a rectangle"""

class Rectangle:
	"""An empty rectangle class"""
	def __init__(self, width=0, height=0):
		"""This initializes a new Rectangle.

        	Args:
            		width (int): for the width of the new rectangle.
            		height (int): for the height of the new rectangle.
		"""
		self.width = width
		self.height = height

	@property
	def width(self):
		"""This retrieves the width attribute"""
		return self.__width

	@width.setter
	def width(self, value):
		"""This sets the width attribute"""
		if not isinstance(value, int):
			raise TypeError("the width must be in integer")
		if value < 0:
			raise ValueError("the width must be >=0")
		self.__width = value

	@property
	def height(self):
		"""This retrieves the height attribute"""
		return self.__height

	@height.setter
	def height(self, value):
		"""This sets the height attribute"""
		if not isinstance(value, int):
			raise TypeError("the height must be an integer")
		if value < 0:
			raise ValueError("the height must be >=0")
		self.__height = value
