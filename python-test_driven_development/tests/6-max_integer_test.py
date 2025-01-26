#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_list_in_order(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_not_order(self):
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        self.assertEqual(max_integer(), None)

    def test_a_string(self):
        self.assertEqual(max_integer("Hello"), "o")
