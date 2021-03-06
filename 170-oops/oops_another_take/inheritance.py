#!/usr/bin/env python3

"""
	Hyundai -> Car
	Hyundai is Car
	Hyundai Extends Car
	Hyundai inherits Car
"""

class Car:

	def __init__(self, color, year):
		self.color = color
		self.year = year

	def display(self):
		print(self.color)
		print(self.year)

class Hyundai(Car):

	def __init__(self, color, year, model):
		super().__init__(color, year)
		self.model = model

	def display(self):
		super().display()
		print(self.model)


c = Hyundai("white", "2021", "elantra")
c.display()

class DangerZone(Exception):
    def __init__(self ,message):
        if message == "mountain":
            Exception.__init__(self, "Broken road ahead")
        else:
            super().__init__("Don't drive above 30")

raise DangerZone("Road")
