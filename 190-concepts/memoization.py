#!/usr/bin/env python3

"""
Recursion: A rescursive function is a function that calls itself

Memoization: Store the value of recent fuction calls so that future calls
dont have to repeat the work
- Explicit
- Using a python function

"""
# Normal Recursion

def fibonacci(n):
    """
        1, 1, 2, 3, 5, 8, 13
    IN: 3
    OUT: 2
    """
    if type(n) != int:
        raise TypeError("N must be integer")
    if n < 1:
        raise ValueError("N must be positive integer")
    if n == 1 or n == 2:
        return 1
    return fibonacci(n- 1) + fibonacci(n -2)

for i in range(1, 31):
    print(i, ": ", fibonacci(i))
    if i == 30:
        break

print()
# Explicit Recursion using memoization

cache = {}

def fib_mem(n):
    if type(n) != int:
        raise TypeError("N must be integer")
    elif n < 1:
        raise ValueError("N must be positive integer")
    if n in cache:
        return cache[n]
    if n == 1 or n == 2:
        value = 1
    else:
        value = fib_mem(n-1) + fib_mem(n -2)
    cache[n] = value
    return value

for i in range(1, 31):
    print(i, ": ", fib_mem(i))


print()
# Recursion using lru_cache

from functools import lru_cache
@lru_cache(maxsize=1000)

def fibonacci(n):
    """
        1, 1, 2, 3, 5, 8, 13
    IN: 3
    OUT: 2
    """
    if type(n) != int:
        raise TypeError("N must be integer")
    if n < 1:
        raise ValueError("N must be positive integer")
    if n == 1 or n == 2:
        return 1
    return fibonacci(n- 1) + fibonacci(n -2)

for i in range(1, 31):
    print(i, ": ", fibonacci(i))
    if i == 30:
        break
