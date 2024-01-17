#!usr/bin/python3
"""The Rectangle Module
   And contain a class rectangle that inherit from the Base class in another module
"""

from models.base import Base

class Rectangle(Base):
	"""Rectangle class that inherit from the base class"""

	def __init__(self, width, height, x=0, y=0, id=None):
		"""The function that initialize a new rectangle
			
		   Args:
			width: the width of the function
			height: the height of the function
			x: the x coordinate
			y: the y coordinate
			id: the optional id
		   
		   Raises:
			TypeError: if width is not an integer
			ValueError: if width is not > 0
			TypeError: if height is not an integer
                        ValueError: if height is not > 0
			TypeError: if x is not an integer
                        ValueError: if x is not >= 0
                        TypeError: if y is not an integer
                        ValueError: if y is not >= 0
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
		if type(value) !=  int:
			raise TypeError('width must be an integer')
		if value <=  0:
			raise ValueError('width must be > 0')
		self.__width = value

	# Getter and setter for height
	@property
	def height(self):
		"""Return the value of the height"""
		return self.__height

	@height.setter
	def height(self, value):
		"""Set the value of the height"""
		if type(value) != int:
			raise TypeError('height must be an integer')
		if value <= 0:
			raise ValueError('height must be > 0')
		self.__height = value

	# Getter and setter fo x
	@property
	def x(self):
		"""Return the value of the x coordinate"""
		return self.__x

	@x.setter
	def x(self, value):
		"""Set the value of the x coordinate"""
		if type(value) != int:
			raise TypeError('x must be an integer')
		if value < 0:
			raise ValueError('x must be >= 0')
		self.__x = value

	# Getter and setter of y
	@property
	def y(self):
		"""Return the value of the y coordinate"""
		return self.__y

	@y.setter
	def y(self, value):
		"""Set the value of the y coordinate"""
		if type(value) != int:
			raise TypeError('y must be an integer')
		if value < 0:
			raise ValueError('y must be >= 0')
		self.__y = value
