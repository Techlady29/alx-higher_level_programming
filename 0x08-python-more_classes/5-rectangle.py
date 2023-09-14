#!/usr/bin/python3
"""This defines a rectangle"""

class Rectangle:
	"""This empty class represents a rectangle"""
	def __init__(self, width=0, height=0):
		""" Instantiation with optional width and height"""
		self.width = width
		self.height = height

	@property
	def width(self):
		""" width"""
		return self.__width
	
	@property
	def height(self):
		""" height"""
		return self.__height

	@width.setter
	def width(self, value):
		""" width sette"""		
		if type(value) is not int:
			raise TypeError("the width must be an integer")
		if value < 0:
			raise ValueError("the width must be >= 0")
		self.__width = value

	@height.setter
	def height(self, value):
		"""height setter"""
		if type(value) is not int:
			raise TypeError("the height must be an integer")
		if value < 0:
			raise ValueError("the height must be >= 0")
		self.__height = value

	def area(self):
		""" returns rectangle area"""
		return self.__width * self.__height

	def perimeter(self):
		""" returns rectangle perimiter"""
		if self.__width is 0 or self.__height is 0:
			return 0
		return self.__width * 2 + self.__height * 2

	def __str__(self):
		""" returns the rectangle with the character"""
		if self.__width is 0 or self.__height is 0:
			return ""
		return ("\n".join(["".join(["#" for a in range(self.__width)])
		for c in range(self.__height)]))

	def __repr__(self):
		""" returns a string represents of the rectangle"""
		return "Rectangle({}, {})".format(self.__width, self.__height)

	def __del__(self):
		"""printing the message when an instance of Rectangle is deleted"""
		print("Bye rectangle...")
