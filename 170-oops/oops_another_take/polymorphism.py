#!/usr/bin/env python3
"""
Polymorphism
Poly Mprphic - Many Forms
or Multiple/Different Behavior

The difference in behaviour of a fuction based on the data or object the function is dealing with is called
polymprphism

- duck typing
- duck typing to dependency injecction (inject one object into another)
- operator overlaoding
- method override to do runtime polymprphism


"""

"Duck Typing"
class Duck:
	def speak(self):
		print("Quack Quack")

class Human:
	def speak(self):
		print("Hello")

"Function behaves differently based on object being passed"

def callSpeak(obj):
	obj.speak()

d = Duck()
h = Human()
callSpeak(d)
callSpeak(h)

"Duck Typing to do dependency injection"
"Use one object into another as a field"

class Flight:

	def __init__(self, engine):
		self.engine = engine

	def start(self):
		self.engine.start()


class Boeing:
	def start(self):
		print("Boeing Engine Starting")	

class Airbus:
	def start(self):
		print("Airbus Engine Starting")	

b = Boeing()
a = Airbus()

Flight(b).start()
Flight(a).start()
