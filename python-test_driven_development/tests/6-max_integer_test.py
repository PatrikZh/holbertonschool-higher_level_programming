#!/usr/bin/python3
""" Unittest testing the maxium integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def testMax(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([-1, -2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer([8, 2, 6, 4]), 8)
        self.assertAlmostEqual(max_integer([1, 2, 7, 4]), 7)
        self.assertAlmostEqual(max_integer([3]),  3)

