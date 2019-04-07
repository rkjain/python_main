#!/usr/bin/env python3

'''
pylint: check code for possible styling convention rules (PEP8), and errors
unittest: test code with unittest
pylint <file_name>.py, comments in the beginning (single string), imporve
scores
usage: python3 -m pylint pylint_style_check.py
'''
def test_print():
    '''
    print's value
    '''
    first = 1
    second = 2
    print(first + second)

if __name__ == "__main__":
    test_print()
