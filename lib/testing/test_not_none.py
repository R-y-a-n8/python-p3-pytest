#!/usr/bin/env python3

import unittest
from not_none_functions import return_not_none

class TestNotNoneFunctions(unittest.TestCase):
    def test_return_not_none(self):
        '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
        result = return_not_none()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()

