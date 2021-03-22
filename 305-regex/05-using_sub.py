#!/usr/bin/env python3
import re

sent = "Agent Rick meets Agent Rita"

ro = re.compile(r'Agent (\w+)')
print(re.findall(ro, sent))

ro_a = re.compile(r'Agent (\w)(\w+)')
print(re.findall(ro_a, sent))

new_sent = re.sub(ro_a, r'Agent: \1***', sent)
print(new_sent)
print(sent)


