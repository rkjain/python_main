'''
Inheritance
  - Square IS-A Shape
    Class Square(Shape)
  - usage of super
  - types:
    - single inheritance Car(Vehicle)
    - multi level inheritance Car(Vehicle), Hybrid(Car)
    - hiearchical inheritance Car(Vehicle), Truck(Vehicle)
    - multiple inheritance HybridEngine(Combustion Engine, ElecticEngine)
    - hybrid inheritance 
      CombustionEngine(Engine), ElectricEngine(Engine)
      HybridEngine(CombustionEngine, ElectricEngine) 
  - Derived Class Canot Modify Base Class's private attributes (encapsulation)

'''

class Car(object):

	def __init__(self, make):
		self.make = make

	def print_details(self):
		print(self.make)


class Elantra(Car):

	def __init__(self, make, model):
		Car.__init__(self, make)
		self.model = model

	def print_details(self):
		Car.print_details(self)
		print(self.model)


class Toyota(Car):

	def __init__(self, make, doors):
		super().__init__(make)
		self.doors = doors


	def print_details(self):
		super().print_details()
		print(self.doors)

car1 = Car('2017')
car1.print_details()

car2 = Elantra('2019', 'Hybrid Sonata')
car2.print_details()


car3 = Toyota('2019',5)
car3.print_details()
