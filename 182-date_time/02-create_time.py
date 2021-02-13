#!/usr/bin/env python3

from datetime import date, time, datetime

d = date(2021,2,1)
t = time(22,50,3)
dt = datetime.combine(d,t)
print(dt)

# Date Objects can be sorted

d1 = date(2032,2,1)
d3 = date(2019,2,1)

x = []
x.append(d1)
x.append(d3)
print(x)
for i in sorted(x):
    print(i)

