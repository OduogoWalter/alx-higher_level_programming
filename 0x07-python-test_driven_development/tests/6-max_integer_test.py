#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reverse_list(self):
        """Test with a reverse list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_mixed_list(self):
        """Test with a mixed list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """Test with a one-element list"""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -10]), -1)

    def test_float_numbers(self):
        """Test with a list of float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_duplicate_numbers(self):
        """Test with a list containing duplicate numbers"""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_mixed_types(self):
        """Test with a list containing mixed types"""
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3, 4])

if __name__ == '__main__':
    unittest.main()
