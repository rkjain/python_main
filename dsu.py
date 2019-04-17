#!/usr/bin/env python3
#Decorate: Create  a list if tuples
#Sort: Use the sort function on the list of tuples
#Undecorate: Iterate and add the items to a list

def dsu(given_string):
    stg = given_string
    empty = []
    for i in stg.split():
        empty.append((len(i),i))
    empty.sort(reverse=True)
    final = []
    print(empty)
    for (k,v) in empty:
        final.append(v)
    return final

print(dsu('Hi My name is rishabh jain, and I am looking at tuples'))
