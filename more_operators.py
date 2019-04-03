#!/usr/bin/env python3
# Generator: Function that generates info rather than saving it in memory
from random import randint
from random import shuffle

#Range
print(list(range(1,11)))
print(list(range(0,10,2)))

#Zip
list_1 = [10,20,30,40]
list_2 = ['a','b','c','d']
list_3 = ['bob','david','marley','davis']
print(list(zip(list_1,list_2,list_3)))

#Enumerate
for item in enumerate('bob'):
    print(item)

for item in enumerate(['bob','david','hazy']):
    print(item)
#In
print('abc' in 'abcdef')
print('abc' in ['abc','def'])

#Min/Max
print(min([5,12,14,3,1]))
print(max([5,12,14,3,1]))

#Random
print(randint(1,5)) # Includes 1 and 5
shuffle(list_1)
print(list_1)

#Input
age = int(input('Can you enter your age ? '))
print(type(age))


