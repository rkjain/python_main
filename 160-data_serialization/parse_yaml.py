#!/usr/bin/env python3
import yaml

with open('sample_yaml.yml') as fd:
    data = yaml.full_load(fd)
    print(data)

# Convert yaml, and do pretty print

print(yaml.dump(data,allow_unicode=True))
