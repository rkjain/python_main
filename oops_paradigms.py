#!/usr/bin/env python3
# Inheritance: Class Dog Extends or Inherits from Animal CLass
# Polymorphism: 2 Objects from differect class can have same method names
class Animal():

    # Protected, Private, And Public Class Attributes
    _location = 'zoo'       # Accessible From Outside
    __height = 2            # Not Accessible From Outside
    country = 'Africa'      # Accessibe From Outside

    def __init__(self):
        self.__legs = None
        self.__tail = None

    def pA(self):
        print('Class Attributes')
        print(self._location)
        print(self.__height)
        print(self.country)

    def set_legs(self):
        self.__legs = 4
        self.__tail = 1

    def get_info(self):
        print(self.__legs)
        print(self.__tail)

    def _pprivate(self):
        print('Private')

    def __pprotect(self):
        print('Protected')

class Dog(Animal):
    def __init__(self,mode='Loud'):
        Animal.__init__(self)
        self.voice = mode

    def get_info(self):
        Animal.get_info(self)
        print(self.voice)

# Create Instance Animal
the_hen = Animal()
the_hen.set_legs()
the_hen.get_info()
the_hen.pA()
the_hen._pprivate()
the_hen._Animal__pprotect()

# Create Instance Dogs

the_dog = Dog('Not that loud')
the_dog.set_legs()

print(the_dog.country)
print(the_dog._location)
print(the_dog._Animal__height)
the_dog.get_info()
the_dog._pprivate()
the_dog._Animal__pprotect()
