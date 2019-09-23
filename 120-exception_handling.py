#!/usr/bin/env python3
# Look for built in errors in python documentation
# Syntax Error and Exception Error
# Raising an Exception
# assert a condition is met or raise Assertion Error

# assert
import sys
assert('darwin' in sys.platform), "This code runs in mac only"

#raise
try:
    raise Exception("You have entered an invalid number")
except Exception as exc:
    ##Printing Exception Name
    print('Exception Name: ',exc.__class__.__name__)
    print('Message: ',exc)


# try,except,else finally
try:
    x = int(input("Enter a number here: "))
except ValueError as err:
    print('You might not have entered a number')
    print('Error Encountered')
    print(dir(err))
    print(err)
else:
    print('I did not go through exception ')
finally:
    print('Finally: Running Post Check')


# Creating Custom Exception

class MyFudgedUpException(Exception):

    def __init__(self, age):
        self.age = age
        if age < 18:
            super().__init__(f'Error Code Young: {self.age}')
        else:
            super().__init__(f'Error Code Old: {self.age}')


age = 23
#raise Exception('Some Kind of Exception')

raise MyFudgedUpException(age)