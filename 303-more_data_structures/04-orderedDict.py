#!/usr/bin/env python3

from collections import OrderedDict

my_dict = OrderedDict()

my_dict['name'] = 'bob'
my_dict['age'] = '29'
my_dict['height'] = '5, 11'

for k, v in my_dict.items():
    print(k, ' => ', v)

