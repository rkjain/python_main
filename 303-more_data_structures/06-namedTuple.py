#!/usr/bin/env python3

from collections import namedtuple

environment = namedtuple('environment',['hostname','ip','user_name'])
staging = environment('staging-myserver','192.168.0.11','root')
production = environment(hostname='prod-1a',ip='192.16.0.23',user_name='root')

print(staging.hostname)
print(staging.ip)
print(staging.user_name)

print("")

print(production.hostname)
print(production.ip)
print(production.user_name)
