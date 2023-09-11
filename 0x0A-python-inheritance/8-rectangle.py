#!/usr/bin/python3

"""this Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
	"""this represent a rectangle using BaseGeometry."""
	def __init__(self, width, height):
		"""this intializes a new Rectangle"""
		self.integer_validator("width", width)
		self.__width = width
		self.integer_validator("height", height)
		self.__height = height
