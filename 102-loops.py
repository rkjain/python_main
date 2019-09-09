#!/usr/bin/env python3
#Iterator: An object that you can iterate over

def print_something():
    pass
print_something()

for i in range(1,11):
    if i == 10:
        break
    print(i)


print('\nWhile')
x = 0
while x < 10:
    if x == 0:
        x += 1
        continue
    else:
        print(x)
        x += 1
