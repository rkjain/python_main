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



def get_square(n):
	my_list = []
	for i in n:
		my_list.append(i * i)
	return my_list


print(get_square([1,2,3,4,5,6,7]))
print(type(get_square([1,2,3,4,5,6,7])))


def yield_square(n):
	for i in n:
		yield i*i

x = yield_square([1,2,3,4,5,6,7])
print(type(x))


for i in x:
	print(i)


some_list = (x*x for x in [5,4,3,2,1])
print(type(some_list))

for i in some_list:
	print(i)

