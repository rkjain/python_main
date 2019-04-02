#!/usr/bin/env python3

class Sample(object):

    wheels = 4
    def __init__(self,name):
        self.name = name
    def test(self):
        x = 2
        y = 3
        print(x * y)
    def test1(self):
        print(self.wheels)

    @staticmethod
    def make_sound():
        print('vovovov')

something = Sample('rishabh')
something.make_sound()
