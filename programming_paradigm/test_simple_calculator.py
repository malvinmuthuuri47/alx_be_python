"""
This module defines a test class for the SimpleCalculator class
"""

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(2, 0), 2)
        self.assertEqual(self.calc.add(1.5, 1.2), 2.7)
        self.assertRaises(TypeError, self.calc.add, 15, "33")
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, 2, )

    def test_subtraction(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(1, 5), -4)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(1.5, 2.8), -1.2999999999999998)
        self.assertRaises(TypeError, self.calc.subtract, )
        self.assertRaises(TypeError, self.calc.subtract, 1, )
        self.assertRaises(TypeError, self.calc.subtract, 1, "er")
        self.assertRaises(TypeError, self.calc.subtract, 1, None)

    def test_multiplication(self):
        """Test the multiply function"""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(-5, 1), -5)
        self.assertEqual(self.calc.multiply(-5, -1), 5)
        self.assertEqual(self.calc.multiply(5.5, 1.6), 8.8)
        self.assertEqual(self.calc.multiply(2, "e"), "ee")
        self.assertRaises(TypeError, self.calc.multiply, 2, )
        self.assertRaises(TypeError, self.calc.multiply, None, 2)

    def test_division(self):
        """Test the divide function"""
        self.assertEqual(self.calc.divide(2, 4), 0.5)
        self.assertEqual(self.calc.divide(2, 0), None)
        self.assertEqual(self.calc.divide(-6, 3), -2.0)
        self.assertEqual(self.calc.divide(-6, -3), 2.0)
        self.assertRaises(TypeError, self.calc.divide, -6, "ee")
        self.assertRaises(TypeError, self.calc.divide, -6, None)
        self.assertRaises(TypeError, self.calc.divide, -6, )
