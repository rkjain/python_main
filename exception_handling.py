#!/usr/bin/env python3
# Look for built in errors in python documentation
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
