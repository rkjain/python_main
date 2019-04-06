#!/usr/bin/env python3

class Sample(object):
    '''
    DOCSTRING:
    INPUT:
    OUTPUT:
    '''
    #class attributes can be accessed with out instatiating the class
    wheels = 4

    #Constructor

    def __init__(self,name='bob'):
    #Object Attrirbute
        self.name = name

    #Magic Methods

    def __str__(self):
        return 'This is what happens when you try to print the object'

    def __len__(self):
        return len('something')

    def __del__(self):
        print('deleting the object')

    #Methods
    def test(self,number=3):
        x = 2
        y = 3
        print(x * y * number)

    def test1(self):
        print(self.wheels)

    def do_math(self,count):
        return 20 + count


    #Static Method
    @staticmethod
    def make_sound():
        print('vovovov')


## Access class variables, before instantiating the object
print(Sample.wheels)
Sample.class_variable = 15
print('Class Attribute', Sample.class_variable)


something = Sample(name='Rishabh')
print(dir(something))
print(something)
something.test_value = 56
print(something.test_value)
print(something.__doc__)
print(something.__dict__)
print(something.__module__)
print(len(something))
something.test()
something.make_sound()
print(something.do_math(25))
del something
