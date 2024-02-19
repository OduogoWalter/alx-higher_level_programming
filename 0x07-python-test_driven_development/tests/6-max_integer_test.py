#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    
    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_numbers(self):
        """Test with a list containing positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-4, 3, -2, 1]), 3)

    def test_single_element_list(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([7]), 7)

    def test_float_numbers(self):
        """Test with a list containing float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5]), -1.5)

if __name__ == '__main__':
    unittest.main()
