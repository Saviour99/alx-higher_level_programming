#!/usr/bin/python3
"""Unittest for models/rectangle.py"""

from models.rectangle import Rectangle
from models.base import Base
import unittest

class TestRectangle_instantiaion(unittest.TestCase):
        """The class for the unittest"""
        def test_no_args(self):
                with assertRaises(TypeError):
			Rectangle()
	def test_one_arg(self):
		with assertRaises(TypeError):
			Rectangle(3)
	def test_two_args(self):
		t1 = Rectangle(4, 20)
		t2 = Rectangle(7, 78)
		self.assertEqual(t1.id, t2.id - 1)
	def test_three_args(self):
		t1 = Rectangle(1,3,67)
		t2 = Rectangle(6, 90, 32)
		self.assertEqual(t1.id, t2.id - 1)
	def test_four_args(self):
                t1 = Rectangle(10, 33, 7, 44)
                t2 = Rectangle(67, 9, 2, 65)
                self.assertEqual(t1.id, t2.id - 1)
	def test_five_args(self):
		self.assertEqual(7, Rectangle(4, 6, 0, 0, 7).id)
	def test_above_five_args(self):
		with self.assertRaises(TypeError):
			Rectangle(1, 2, 3, 4, 5, 6)

	def test_width_private(self):
		with self.assertRaises(TypeError):
			Rectangle(5, 8, 0, 0, 9).__width
	def test_height_private(self):
                with self.assertRaises(TypeError):
                        Rectangle(5, 8, 0, 0, 9).__height
	def test_x_private(self):
                with self.assertRaises(TypeError):
                        Rectangle(5, 8, 0, 0, 9).__x
	def test_y_private(self):
                with self.assertRaises(TypeError):
                        Rectangle(5, 8, 0, 0, 9).__y
	
	def test_width_getter(self):
		w = Rectangle(9, 9, 1, 1, 5)
		self.assertEqual(9, w.width)
	def test_width_setter(self):
                w = Rectangle(4, 6, 2, 2, 9)
                w.width = 50
                self.assertEqual(w.width, 50)
	def test_height_getter(self):
                h = Rectangle(9, 9, 1, 1, 5)
                self.assertEqual(9, h.height)
	def test_height_setter(self):
                h = Rectangle(4, 6, 2, 2, 9)
                h.height = 50
                self.assertEqual(h.height, 50)
	def test_x_getter(self):
                x = Rectangle(9, 9, 1, 1, 5)
                self.assertEqual(1, x.x)
	def test_x_setter(self):
                x = Rectangle(4, 6, 2, 2, 9)
                x.x = 13
                self.assertEqual(x.x, 13)
	def test_y_getter(self):
                y = Rectangle(9, 9, 1, 1, 5)
                self.assertEqual(1, y.y)
	def test_y_setter(self):
		y = Rectangle(4, 6, 2, 2, 9)
		y.y = 5
		self.assertEqual(y.y, 5)

def __init__ = "__main__":
        unittest.main()
