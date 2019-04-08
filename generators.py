#!/usr/bin/env python3
# Generator is a function that creates an iterator
# Anything that you can iterate over is an  iterable
# For loop allows us to iterate over an iterable or a iterator

def genSquare(n):
    for number in range(1, n + 1):
        yield number * number

my_gen = genSquare(6)
print(type(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

#for i in my_gen:
#    print(i)


my_list= [1,2,3,4,5,6]
type(my_list)
itr_my_list = iter(my_list)
print(next(itr_my_list))
print(next(itr_my_list))
print(next(itr_my_list))
print(next(itr_my_list))
print(next(itr_my_list))
print(next(itr_my_list))
