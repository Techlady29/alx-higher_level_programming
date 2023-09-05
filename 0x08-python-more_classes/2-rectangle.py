#!/usr/bin/python3

"""This defines a rectangle"""

class Rectangle:
	"""This represents a rectangle"""
	def __init__(self, width=0, height=0):
		"""This initializes the rectangle"""
	self.width = width
	self.height = height

	@property
	def width(self):
		"""this gets the private instance attribute width"""
		return self.__width

	@width.setter
	def width(self, value):
	 	"""sets the private instance attribute width"""
	if type(value) is not int:
		raise TypeError("the width must be an integer")
	if value < 0:
		raise ValueError("the width must be >= 0")
	self.__width = value

	@property
	def height(self):
        	"""gets the private instance attribute height"""
return self.__height

@height.setter
def height(self, value):
	 	"""sets the private instance attribute height"""
if type(value) is not int:
raise TypeError("the height must be an integer")
	if value < 0:
		raise ValueError("the height must be >= 0")
	self.__height = value

	def area(self):
	 	"""this returns the area of the rectangle"""	
	return self.__width * self.__height

	def perimeter(self):
	 	"""this returns the perimeter of the rectangle"""
	if self.__width == 0 or self.__height == 0:
		return 0
	return (self.__width * 2) + (self.__height * 2)
