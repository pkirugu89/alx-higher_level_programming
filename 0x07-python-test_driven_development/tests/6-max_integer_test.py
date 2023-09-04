#!/usr/bin/python3
""" Unittest for max integers. """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class that defines max_integer. """
    def test_ordered_list(self):
        """ Test an ordered integer lists."""
        ordered_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered_list), 4)

    def test_unordered_list(self):
        """ Test an unordered integer list."""
        unordered_list = [1, 4, 2, 3]
        self.assertEqual(max_integer(unordered_list), 2)

    def test_max_at_beginning(self):
        """Test a list with a beginning max value."""
        max_at_start = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_start), 3)

    def test_one_element_list(self):
        """ Test a list with 1 element."""
        element_1 = [7]
        self.assertEqual(max_integer(element_1), 7)

    def test_floats(self):
        """ Test a list of floats."""
        floats = [1.23, 6.32, -10.35]
        self.assertEqual(max_integer(floats), 6.32)

    def test_ints_and_floats(self):
        """ Test a list of ints and floats."""
        int_floats = [1.63, 14.7, 98, -5]
        self.assertEqual(max_integer(int_and_floats), 14.7)

    def test_strings(self):
        """ Test a list of strings. """
        str = ["Tom", "Clancy", "Jack", "Ryan"]
        self.assertEqual(max_integer(str), "Jack")

    def test_empty_string(self):
        """ Test an empty string."""
        self.assertEqual(max_integer(""), None)

    if __name__ == '__main__':
        unittest.main()
