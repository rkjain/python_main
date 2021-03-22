#!/usr/bin/env python3
import re

number = 'my number is 123-456-8901, and second number is 987-123-4321'
mo = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', number)
if mo:
    print(mo.group())
ro = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

print(re.findall(r'\d\d\d-\d\d\d-\d\d\d\d', number))
print(re.findall(ro, number))
