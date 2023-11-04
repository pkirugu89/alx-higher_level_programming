#!/usr/bin/python3
"""
===================================
Module for max_integer() function
===================================
"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Method for finding a max integer in a list. """

    def test_empty_list(self):
        """ Test with an empty list."""
        self.assertIsNone(max_integer([]), '')

    def test_single_element_list(self):
        """ Testing a single element in a list."""
        self.assertEqual(max_integer([42]), 42)

    def test_positive_numbers(self):
        """ Testing with positive numbers."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        """ Testing with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        """ Testing with mixed numbers."""
        self.assertEqual(max_integer([-1, 2, 0, -4, 5]), 5)

    def test_float_numbers(self):
        """ Testing with floating point numbers."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4, 5.5]), 5.5)

    def test_string_list(self):
        """ Testing with string list."""
        self.assertEqual(max_integer(['apple', 'banana', 'cherry']), 'cherry')
