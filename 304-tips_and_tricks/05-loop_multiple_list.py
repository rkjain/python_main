#!/usr/bin/env python3

listA = [10, 20, 30]
listB = [40, 50, 60, 70]
listC = [80, 90, 100 ]

print(listA)
print(listB)
print(listC)

for val1, val2,val3 in zip(listA, listB, listC):
    print(val1, val2, val3)
