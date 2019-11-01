#!/usr/bin/env python3.7

def run_me(name: str) -> str:
    x: int = 3
    print(x)
    return f'My name is {name}'

print(
    run_me('rishabh')
)


"""
C:\Users\some_user\Desktop>py -3 -m mypy type_hints.py
Success: no issues found in 1 source file

C:\Users\some_user\Desktop>py -3 -m mypy type_hints.py
type_hints.py:2: error: Incompatible types in assignment (expression has type "int", variable has type "str")
Found 1 error in 1 file (checked 1 source file)


"""
