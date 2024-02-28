#!/usr/bin/python3
"""Unit tests for Base module."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init(self):
        obj = Base()
        self.assertIsNotNone(obj.id)

    def test_to_json_string(self):
        obj = Base()
        json_string = obj.to_json_string()
        self.assertIsInstance(json_string, str)

    # Add more test cases as needed


if __name__ == "__main__":
    unittest.main()
