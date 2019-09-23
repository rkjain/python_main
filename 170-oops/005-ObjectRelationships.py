'''
 Class Relationship
 - IS A (Inheritance)
 - HAS A (Aggregation)
   -  One Class Has Object of Another
   - Class Person HAS A Object Of Class Country
 - Composition
   Class Laptop is composed of processor and speakers

'''

class Country(object):

	def __init__(self, name, population):
		self.name = name
		self.population = population

	def print_details(self):
		print(self.name)
		print(self.population)

country1 = Country('ireland', 49000000)
country1.print_details()
print()


class Person(object):
	def __init__(self, name, country):
		self.name = name
		self.country = country
	def print_details(self):
		print(self.name)
		self.country.print_details()

person1 = Person('bobby', country1)
person1.print_details()



class Processor(object):
	def __init__(self, speed):
		self.speed = speed
	def print_details(self):
		print(self.speed)

class Speaker(object):
	def __init__(self, name):
		self.name = name
	def print_details(self):
		print(self.name)
class Laptop(object):
	
	def __init__(self, speed, speaker_comp):
		self.processor =  Processor(speed)
		self.speaker = Speaker(speaker_comp)

	def print_details(self):
		self.processor.print_details()
		self.speaker.print_details()

print()
hp = Laptop('64-bit','Altec Lensing')
hp.print_details()
