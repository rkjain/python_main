#!/usr/bin/env python3

from collections import defaultdict

x = defaultdict(lambda: 'hello World')

print(
        x['default_greeting']
)
