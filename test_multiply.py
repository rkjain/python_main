#!/usr/bin/env python3
import unittest
import multiply
'''
name of the test module is test followed by "_" followed by the module to test
we create a class called Test Followed by in caps the name of the module to test
'''

class TestMultiply(unittest.TestCase):
    '''
    Create 2 functions 
    '''
    def test_product(self,a=2,b=4):
        prodOne = multiply.multiply_num(a,b)
        prodTwo = 8
        self.assertEqual(prodOne, prodTwo)

    def test_product_double(self,a=20,b=20):
        prodOne = multiply.multiply_num(a,b)
        prodTwo = 400
        self.assertEqual(prodOne, prodTwo)

if __name__ == '__main__':
    unittest.main()

