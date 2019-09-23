from abc import ABC, abstractmethod

'''
  Polymorphism
    - using methods
    - using inheritance
      base class method has pass, and is overwritten in the derived class
    - method overriding
    - operator overloading

  List of special functions

    - __add__  		+
    - __sub__  		-
    - __truediv__ 	/ 
    - __mul__ 		*
    - __lt__ 		<
    - __gt__ 		>
    - __eq__  		==
  
  Polymorphism Using Dynamic Typing
    - Dynamic Typing, Type of an oject can be changed later
    - Duck Typing to create polymorphism

  Abstract Base Classes
'''

class Rectangle():

	def area(self):
		return 'length * breadth'

class Circle():

	def area(self):
		return '3.14 * square(radius)'


sample1 = Rectangle()
sample2 = Circle()

print(sample1.area())
print(sample2.area())


class Concatenate(object):

	def __init__(self, string1):

		self.string1 = string1


	def __add__(self, other):
		return self.string1 + ' plus ' + other.string1

	def __sub__(self, other):
		return self.string1 + ' minus ' + other.string1


obj1 = Concatenate('Rishabh')
obj2 = Concatenate('Jain')
obj3 = obj1 + obj2
obj4 = obj1 - obj2


print(obj3)
print(obj4)


## Polymorphism Using Duck Typing
# Since Animal Cat and Dog, can both speak as animals
# Cats and Dogs are both animals


class Cat(): 
	def speak(self):
		print('Meow Meow')

class Dog():
	def speak(self):
		print('Woof Woof')

class Animal():
	def Sound(self, animal):
		animal.speak()

animal1 = Animal()
animal1.Sound(Cat())
animal1.Sound(Dog())





class Environment(ABC):
  @abstractmethod
  def ip(self):
    pass

  @abstractmethod
  def name(self):
    pass

class DitOne(Environment):
  def ip(self):
    pass
  def name(self):
    pass
  def hello(self):
    pass

x = DitOne()

print(type(x))