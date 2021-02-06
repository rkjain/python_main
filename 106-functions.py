#!/usr/bin/env python3
from functools import reduce

#Basics
def print_name(name='rishabh'):
    '''
    DOCSTRING: prints name passed as a parameter
    INPUT: name (string)
    OUTPUT: Aloha Rishabh (string)
    '''
    return 'Aloha ' + name

x = print_name
#help(x)
print(x())

#args and kwargs

def trick_func(*args, **kwargs):
    print('args: ')
    print(args)
    for item in args:
        print(item)
    print('kwargs: ')
    print(kwargs)
    for elem in  kwargs:
        print(elem)

trick_func()
trick_func(10,20)
trick_func(name='rishabh',age='20')
trick_func(12,14,name='rishabh',age='20')


#Lambda Expression
#Annonymous Functions
print_name_l = lambda name: 'Hello ' + name
print(print_name_l('Rishabh Kumar Jain'))

# Map, Reduce, Filter                                                             
                                                                                  
# Reduce: returns a value                                                         
print(reduce((lambda x,y: y + x),"hello_world"))                                  
print(reduce((lambda x,y: x + y),[10,20,30,40,50], 100))                          
                                                                                  
# map: returns a gen                                                              
                                                                                  
map_gen = map((lambda x: x ** 2), [5,4,3,2,1])                                    
print(map_gen)                                                                    
print(list(map_gen))                                                              
                                                                                  
# filter: returns a filter object                                                 
print(list(filter((lambda x: x >= 3), [1,2,3,4,5])))  





my_list = [10,20,30,40,50]
my_name = 'rishabh'
new_list  = list(map(lambda number: number + 2, my_list))
new_list1 = list(filter(lambda value: value > 12, my_list))
new_list2 = reduce(lambda x, y : y + x, my_name, "")

print(my_list)
print(new_list)
print(new_list1)
print(new_list2)

#Nested Statements and Scope
#LEGB Local Scope Has Higher Priority > Enclosed > Global > Buit In Scope

number = 45 # Global

def print_number():
    number = 47 # Enclosed
    def print_one_more_number():
        number = 50 #Local
        print(number)
    print_one_more_number()
    def print_enc():
        print(number)
    print('Enclosed Value of Number: ',end= "")
    print_enc()

print('Global Value: ', number) 
print('Local Vlaue: ', end= "")
print_number()
print('Built In', 'int')

# Zip Functions

list_a = ["a", "b", "c", "d", "e"]
list_b = [70, 80, 90, 100, 120, 140]

some_list = list(zip(list_a, list_b))
print(dict(some_list))
