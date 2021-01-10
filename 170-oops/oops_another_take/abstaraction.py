#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Car(ABC):

	def __init__(self, make, model, year):
		ABC.__init__(self)
		self.make = make
		self.model = model
		self.year = year

	@abstractmethod
	def display(self):
		pass

	@abstractmethod
	def start(self):
		print("Starting Car")

class Bmw(Car):

	def __init__(self, make, model, year):
		Car.__init__(self, make, model, year)

	def display(self):

		print(self.make)
		print(self.model)
		print(self.year)

	def start(self):
		Car.start(self)
		print("Starting BMW")

c = Bmw("3series", "i385", 2021)
c.display()
c.start()
