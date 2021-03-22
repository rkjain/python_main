#!/usr/bin/env python3
import re

number = 'my number is 123-456-8901, and second number is (987)-123-4321'
sent = 'batman, batmobile, batcopter, battery, battleship'

ro_a = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
ro_b = re.compile(r'\(\d\d\d\)')

mo_a = re.search(ro_a, number)

if mo_a:
    print('group()', mo_a.group())
    print('group(0)', mo_a.group(0))
    print('group(1)',mo_a.group(1))
    print('group(2)',mo_a.group(2))

mo_b = re.search(ro_b, number)

if mo_b:
    print(mo_b.group())

ro_c = re.compile(r'bat(man|mobile|copter)')
mo_c = re.search(ro_c, sent)
if mo_c:
    print(mo_c.group())
    print(mo_c.group(1))

print(re.findall(ro_c, sent))
