#!/usr/bin/env python3

from time import sleep, perf_counter

t1 = perf_counter()
sleep(10)
t2 = perf_counter()
result = t2 - t1
print(result)
print('Execution Time: ', round(result, 3))
