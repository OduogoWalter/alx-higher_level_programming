#!/usr/bin/python3
"""Unit tests for Base module."""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def test_base_id(self):
        """Test base id."""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_base_id_custom(self):
        """Test base id with custom id."""
        b1 = Base()
        self.assertEqual(b1.id, 3)
        b2 = Base(10)
        self.assertEqual(b2.id, 10)

    # Add more test cases for other methods and classes...

if __name__ == "__main__":
    unittest.main()
