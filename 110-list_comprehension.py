#!/usr/bin/env python3
# Create a list and append items in the list
name = 'rishabh jain'
my_list = []
for char in name:
    my_list.append(char)
print(my_list)

#List Comp Way 1
print([char for char in 'rishabh jain'])
my_list2 = [x for x in range(1,11)]
print(my_list2)

celsius = [0,10,20,30,40]
farenheit = [((9/5) * temp + 32) for temp in celsius]
print(celsius)
print(farenheit)

#if
some_list = [x for x in range(1,15) if x % 2 == 0]
print(some_list)
#if-else
lA = [ (x,'even') if x % 2 == 0 else (x,'odd') for x in range(1,11)]
print(lA)
#2 for loops
lB = [ x * y for x in [1,2,3] for y in [4,5,6]]
print(lB)