#!usr/bin/python3
"""The Rectangle Module
   And contain a class rectangle that inherit from the Base class in another module
"""

from models.base import Base

class Rectangle(Base):
	"""Rectangle class that inherit from the base class"""

	def __init__(self, width, height, x=0, y=0, id=None):
		"""The function with width, height, x, y and id
			
		   Args:
			width: the width of the function
			height: the height of the function
			x: the x coordinate
			y: the y coordinate
			id: the optional id
		"""

		super().__init__(id) # the superclass constructor
		
		self.width = width
		self.height = height
		self.x = x
		self.y = y

	# Getter and sette for width
		
	@property
	def width(self):
		"""Return the value of the width"""
		return self.__width

	@width.setter
	def width(self, value):
		"""Set the value of the width"""
		self.__width = value

	# Getter and setter for height
	@property
	def height(self):
		"""Return the value of the height"""
		return self.__height

	@height.setter
	def height(self, value):
		"""Set the value of the height"""
		self.__height = value

	# Getter and setter fo x
	@property
	def x(self):
		"""Retur the value of the x coordinate"""
		return self.__x

	@x.setter
	def x(self, value):
		"""Set the value of the x coordinate"""
		self.__x = value

	# Getter and setter of y
	@property
	def y(self):
		"""Return the value of the y coordinate"""
		return self.__y

	@y.setter
	def y(self, value):
		"""Set the value of the y coordinate"""
		self.__y = value
