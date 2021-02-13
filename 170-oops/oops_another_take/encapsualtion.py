#!/usr/bin/env python3

"""
Encapsulation provides protection to an object's data/properties from other objects by defining getter/setter methods to access modify the object's data
"""

class Car:

	## Mutator / Setter Method
	def set_make(self, make):
		self.make = make

	## Accessor / Get Method
	def get_make(self):
		return self.make

c = Car()
c.set_make("Hyundai")
print(c.get_make())
