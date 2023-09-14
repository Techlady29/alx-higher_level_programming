#!/usr/bin/python3
"""this defines a class Student"""


class Student:
	"""this represents a student"""

	def __init__(self, first_name, last_name, age):
		"""Initializes a new Student
		"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def to_json(self):
		"""this gets a dictionary representation of the Student"""
		return self.__dict__
