'''
Class
 - properties/variables/data
   - class variables
   - instance variables

 - methods/behaviour
   - class methods
   - instance method
   - static method
   - method overload

 - access modifiers
   - public
   - private
   - not so private

'''

class LightBulb(object):

	# Class property or variables
	manufacture = 'Philips'

	@classmethod
	# access and modify class variables
	def print_manufacture(cls):
		return cls.manufacture

	@staticmethod
	# When you want to use a method that is not bounded to an object
	def bulbSize():
		return "40 * 40"

	def __init__(self):
		# property, data
		# instance variables, you can also use default initializer
		self.__state = 'off' # private_property
		self.id = 23
		print('Bulb State: ', self.__state)

    # private method
	def __get_id(self):
		print(self.id)

	def print_id(self):
		self.__get_id()

	def turnOn(self):
		# instance method
		self.__state = 'on'
		return self.__state

	def turnOff(self):
		# method
		self.__state = 'off'
		return self.__state

	def overload_color(self, a='green'):
		# overloaded method (mem efficient , runs faster, clean code, enables polym)
		self._color = a
		return self._color


# Class Property
print(LightBulb.manufacture)
print(LightBulb.print_manufacture())
print(LightBulb.bulbSize())


bulbOne = LightBulb() #print(bulbOne.manufacture)
bulbOne.print_id()

# Memory Location of the object
#print(bulbOne)

# Methods
print(bulbOne.turnOff())
print(bulbOne.turnOn())


# Create Prop Outside the Class
bulbOne.color = 'green'


#print(dir(bulbOne))

# Overload Color Method
print(bulbOne.overload_color('blue'))
print(bulbOne.overload_color())


# Not So Protected
print(bulbOne._LightBulb__state)
