#!/usr/bin/env python3.7

# String is a immutable object
x = 'rishabh'

print(type(x))

# Print first character
print(x[0])

# Slice 
print(x[0:])
print(x[1:])
print(x[0:2])

# Mention Step Size
print(x[::2])

# reverse a string
print(x[::-1])



s = " Finished ! "
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.count('b'))
print(s.find('m'))
print(s.center(20, '#'))

print(s.isalnum())




x = "bob"
print(x[0])

print(f"Hi, my name is {x}")

"""
x = {
	"name": "bob",
	"age": 23
}



y = x.get("height")

if y is None:
	print("Y is None")

"""