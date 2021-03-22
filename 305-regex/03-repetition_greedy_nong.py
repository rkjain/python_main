#!/usr/bin/env python3
import re

number = 'my number is 123-456-8901,897-632-5123,123-456-7890'

ro = re.compile('(\d{3}-\d{3}-\d{4},?){2,3}?')
ro_z = re.compile('(\d{3}-\d{3}-\d{4},?)')
mo = re.search(ro, number)
if mo:
    print(mo.group())

print(re.findall(ro_z, number))
