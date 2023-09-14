#!/usr/bin/python3
"""this defines a class Student"""


class Student:
	"""this represent a student."""

	def __init__(self, first_name, last_name, age):
		"""this initializes a new Student
		"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def to_json(self, attrs=None):
		"""gets a dictionary representation of the Student
		If attrs is a list of strings, represents only those attributes
		included in the list
		"""
		if (type(attrs) == list and
				all(type(ele) == str for ele in attrs)):
			return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
		return self.__dict__

	def reload_from_json(self, json):
		"""this replaces all attributes of the Student
		"""
		for j, v in json.items():
			setattr(self, j, v)
