#!/usr/bin/env python3

class Guitar:
    """
    0. Constructor
    1. Class has properties and methods
    2. Instance Vairables and Methods
    3. Class Variable and Methods(Static)
    4. Private Variables
    """
    # Class Variables/ Fields
    instances = 0

    # Contructor
    def __init__(self, brand=None):
        Guitar.instances += 1

        # Instance Variables
        # Private: Object._ClasName__variableName
        self.__brand = brand
        self.__strings = 6

    # Instance Method
    def get_details(self):
        print(self.__brand)
        print(self.__strings)

    def helper(self, name):
        return "Hello {name}".format(name=name)

    def greet(self, name):
        """
        Use one instance method to call another
        """
        return self.helper(name)


    # Class Method / Static Method
    @staticmethod
    def get_instances():
        return Guitar.instances

if __name__ == "__main__":

    # Class Variabls and methods can be called with out instantiating the class
    print(Guitar.instances)
    print(Guitar.get_instances())
    g = Guitar("Yamha")
    print(g._Guitar__strings)
    g.get_details()
    b = Guitar("Gibson")
    b.get_details()
    c = Guitar("Fender")
    c.get_details()
    print(c.greet("Bob Marlery"))
    print(g.get_instances())
