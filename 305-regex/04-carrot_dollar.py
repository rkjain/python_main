#!/usr/bin/env python3
import re

test = "HelloWorld"
test_a = "HelloWorld"

number = '1234567897654321'
anum = '12345x78919'

ro = re.compile(r'Hello')
mo = re.search(ro, test)
print(mo.group())

ro_a = re.compile(r'^Hello')
mo_a = re.search(ro_a, test)
if mo_a:
    print(mo_a.group())

ro_c = r'^\d+$'
mo_c = re.search(ro_c, number)

if mo_c:
    print(mo_c.group())
