#!/usr/bin/env python3
# Boolean values are primitives (Note: the capitalization)
True
False

# negate with not
not True   # => False
not False  # => True

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False  # => False
False or True   # => True

# True and False are actually 1 and 0 but with different keywords
True + True # => 2
True * 8    # => 8
False - 5   # => -5

# Comparison operators look at the numerical value of True and False
0 == False  # => True
1 == True   # => True
2 == True   # => False
-5 != False # => True

# Using boolean logical operators on ints casts them to booleans for evaluation, but their non-cast value is returned
# Don't mix up with bool(ints) and bitwise and/or (&,|)
bool(0)     # => False
bool(4)     # => True
bool(-6)    # => True
0 and 2     # => 0
-5 or 0     # => -5

# Equality is ==
1 == 1  # => True
2 == 1  # => False

# Inequality is !=
1 != 1  # => False
2 != 1  # => True

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Seeing whether a value is in a range
1 < 2 and 2 < 3  # => True
2 < 3 and 3 < 2  # => False
# Chaining makes this look nicer
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a             # Point b at what a is pointing to
b is a            # => True, a and b refer to the same object
b == a            # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # => False, a and b do not refer to the same object
b == a            # => True, a's and b's objects are equal



print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(()))


