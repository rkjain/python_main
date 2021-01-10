#!/usr/bin/env python3

class Vehicle:

	# Class Variables/ Fields
	total_instances = 0

	# Constructor/ Instance Variables
	def __init__(self):

		Vehicle.total_instances += 1

		## private variables
		self.__wheels = 4
		self.__steering_wheel = 1

	# instance methods
	def display(self):
		print("Total Wheels: ", self.__wheels)
		print("Steering Wheel: ", self.__steering_wheel)

	# class method/static method
	@staticmethod
	def get_instances():
		return Vehicle.total_instances


v = Vehicle()
print(v._Vehicle__wheels)
v.display()
print("Total Insatances: ", v.get_instances())
