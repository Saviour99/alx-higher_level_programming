#!/usr/bin/python3
"""This is a models module
This module contains a base class
"""

class Base:
	"""The models class: base
	
	Attributes:
		id (int): The unique id
	"""

	__nb_objects = 0  #: Private class attribute
	def __init__(self, id=None):
		"""Initiaizes a base object.

		Args:
			id (int, optional): An optional id
		"""

		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
