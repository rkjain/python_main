#!/usr/bin/env python3


print("yahoo" if 3 > 2 else "bye")

x = [1,2,3]
x.append(4)
print(x)

y = x.pop()
print(y)

x.insert(0,0)
print(x)

y = [4,5,6]

print(x + y)

y.extend(x)
print(y)

print(4 in y)


