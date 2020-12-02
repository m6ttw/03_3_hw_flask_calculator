import unittest

from modules.calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        add_result = add(1, 2)
        self.assertEqual(3, add_result)

    def test_subtract(self):
        subtract_result = subtract(10, 5)
        self.assertEqual(5, subtract_result)

    def test_multiply(self):
        multiply_result = multiply(4, 2)
        self.assertEqual(8, multiply_result)

    def test_divide(self):
        divide_result = divide(10, 2)
        self.assertEqual(5, divide_result)