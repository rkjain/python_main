#!/usr/bin/env python3

#File Operations

# Write
with open('test_file.txt',mode='w') as  fh:
    fh.write('Hi, My  name is rishabh,\nHow are you doing')
# Append
with open('test_file.txt',mode='a') as  fh:
    fh.write('\nAdding More Content')
#Read
with open('test_file.txt') as fh:
    print(fh.read())
