# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right Scalene', '5, 12, 13 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right Scalene', '3, 4, 5 is a right angle scalene')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1,  1), 'Equilateral', '1,1,1 should be equilateral')

    def testIsosceles(self):
        self.assertEqual(classifyTriangle(5, 5, 2), 'Isosceles', '5, 5, 2 is a isosceles')

    def testScalene(self):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene', '2, 3, 4 is a scalene')

    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', '0, 1, 1 is invalid')
        self.assertEqual(classifyTriangle(1, 0, 1), 'InvalidInput', '1, 0, 1 is invalid')
        self.assertEqual(classifyTriangle(1, 1, 0), 'InvalidInput', '1, 1, 0 is invalid')
        self.assertEqual(classifyTriangle(201, 200, 200), 'InvalidInput', '201, 200, 200 is invalid')
        self.assertEqual(classifyTriangle(200, 201, 200), 'InvalidInput', '200, 201, 200 is invalid')
        self.assertEqual(classifyTriangle(200, 200, 201), 'InvalidInput', '200, 200, 201 is invalid')
        self.assertEqual(classifyTriangle(2.8, 3, 1), 'InvalidInput', '2.8, 3, 1 is invalid')
        self.assertEqual(classifyTriangle(2, '^', 1), 'InvalidInput', "2, '^', 1 is invalid")
        self.assertEqual(classifyTriangle(1, 1, 'w'), 'InvalidInput', "1, 1, 'w' is invalid")

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(5, 5, 10), 'NotATriangle', '5, 5, 10 is not a triangle')
        self.assertEqual(classifyTriangle(6, 3, 2), 'NotATriangle', '6, 3, 2 is not a triangle')
        self.assertEqual(classifyTriangle(7, 20, 7), 'NotATriangle', '7, 20, 7 is not a triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
