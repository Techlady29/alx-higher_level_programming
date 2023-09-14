#!/usr/bin/python3
"""This defines a rectangle"""

class Rectangle:
	"""empty class rectangle"""
	def __init__(self, width=0, height=0):
		"""the instantiation with optional width and height"""
		self.width = width
		self.height = height

	@property
	def width(self):
		"""the width"""
		return self.__width

	@property	
	def height(self):
		"""the height"""
		return self.__height

	@width.setter
	def width(self, value):
		"""the  width setter"""
		if type(value) is not int:
			raise TypeError("the width must be an integer")
		if value < 0:
			raise ValueError("the width must be >= 0")
		self.__width = value  

	@height.setter
	def height(self, value):
		"""the height setter"""
		if type(value) is not int:
			raise TypeError("the height must be an integer")
		if value < 0:
			raise ValueError("the height must be >= 0")			
		self.__height = value

	def area(self):
		"""this returns rectangle area"""
		return self.__width * self.__height
	
	def perimeter(self):	
		"""this returns rectangle perimiter"""
		if self.__width is 0 or self.__height is 0:
			return 0
		return self.__width * 2 + self.__height * 2

	def __str__(self):
		""" this return the rectangle with the character"""
		if self.__width is 0 or self.__height is 0:
			return ""
		return ("\n".join(["".join(["#" for i in range(self.__width)])
		for j in range(self.__height)]))
	def __rep r__(self):
		""" this return a string representation of the rectangle"""
		return "Rectangle({}, {})".format(self.__width, self.__height)
