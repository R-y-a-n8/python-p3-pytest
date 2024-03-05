#!/usr/bin/env python3

import unittest
from bool_functions import return_true  # Import the function you want to test

class TestBoolFunctions(unittest.TestCase):
    def test_return_true(self):
        '''in bool_functions, function "return_true" returns True.'''
        self.assertTrue(return_true())

if __name__ == '__main__':
    unittest.main()

