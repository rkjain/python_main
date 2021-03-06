# NOTES

## Declare Variables

## Some Useful Functions
  - print
  - sys.stdout.write
  - sys.stdin.readline
  - bool, type
  - string functions - upper, lower
  - string formatting

## Comments
  - single line
  - multi line

## Datatypes
  - String
  - Integer
  - Float
  - Boolean
  - Sets
  - Dictionary
  - Tuple
  - List

## Operators
  - Logical: and, or, not
  - Comparison Operators
  - Arithmetic: +, -, *, /, // , **, enforce precedence ()


## STRING
- immutable
- str yestype
- type(x)
- single quote , double quote, triple quotes
- 'a' + 4, 'a' * 3
- print() with  use of \
- str.upper() and lower()
- str.split()
- string interpolation x = y + 'jain'
- float formatting and string formatting (value:width.precision)
- print('My name is rishabh {last} and I have {money:1.3f}'.format(last='jain',money=50.3145))
- from (__future__) import print_function


## Numbers
- int, float, typecasting
- + , - , **, /, ** , //
- from decimal import Decimal as d


## Boolean
- True False None

## Variables
- x = 1, x = '', x = '''   '''

## Lists
- mutable
- append, pop (stack)
- append, pop(0) (queue)
- insert(index, value)
- extend
- item in list
- list.join, list.sort, list.reverse
- create a list []
- add [].append()
- add list1 + list2
- slice a list
- remove from a list using .remove(value)
- new_list.sort()(In Place, returns None)
- reverse (In Place, returns None)
- sorted(), returns sorted , reversed returns iterator


## Sets
- unordered collection of data
- hold unique values
- has  add method
- x = set()
- you can also convert a list into a set
- Operations
  - Creation
  - Add Elements
  - Remove/Discard Elements
  - Intersection, Union, Difference, Symetric Difference, Superset/Subset

## Tuples
- Create(10,)
- immutable
- Add new() = old() + (10,20)
- Unpack a tuple into multiple variables x,y,z = tupleSomething
- are like lists and preserver data integrity
- also used with print

## Dictionaries
- keys are ordered in python3
- Use Immutable Keys, don't use lists
- add keys, delete keys using del
- del dict[key], del dict
- dict.pop(key)
- Keys list(dict.keys())
- key in {}
- Values list(dict.values())
- Create dicts dict(key1=10, key2=20)
- Create dicts dict([('age',10),('name','bob')])

## Conditionals
- if / elif / else
- if condition: followed by indented next line
- 2 in / not in [12,20]

## Ternary Operator
- x = 3 if a > b else 3

## Loops

- for , while, usage of break, continue
- usage of pass in a function
- while COND: pass
- continue in the while loop to continue with the  next iteration
- break to break the loop
- pass does nothing
- for var in list/tuple/dict.keys()
- iterate over a list of tuples for x,y in[(10,20),(30,40)]
- iterate over a dict for key,value in dict.items()

## UserInput
- input('Enter a value')
- age = int(input("Enter Age"))

## Functions
- def function_name():
- function can have return value
- args, kwargs , func_a(10, a=3)
- *args is a tuple
- **kwargs is a dictionary
- lambda
  - one line functions, annonymous functions
  - (lambda: print("hello"))()
  - x = lambda: a: a + 3, x(13)
  - age = lambda x, y: x + y, age(12,12)
  - (lambda x, y: x + y)(13,13)
- map, filter, reduce
    - map gives a gen
    - filter give a filter object
    - functools.reduce gives a value
- zip
    - returns a zip object, convert it into a list
    - returs a list of tuple of individual objects
    - zip(['a','b','c'],[10,20,30]) => [(a, 10), (b,20), (c,30)]
- file operations
    - read, write, append

- list_comprehension
  - list comprehensions to emulate map, filter
  - using ternary operators , condtions in lc

- Generators

- Decorators

- Regex
  - look for a substring within a string
  - validate a given string
  - methods in re
    - search (returns None if nothing found)
    - match (looks in the beg, returns None if nothing found)
    - split
    - findall (returns a list , [] if nothing found)
    - sub(replaceall)
  - sequence characters: \d \D \s \S \w \W \b \B
  - special characters: \ , . (any char except \n), ^, $, 
                        [A-Z][aZ][1-9] (R|R2) (R) [^g]
  - quantifiers: {m, n}, {m}, + , *, ?
  
## Applications

- liniting: python3 -m pylint file.py

- unittest
    - functions should start with test
    - create a class that inherits unittest.TestCase
    - to run testcases use unittest.main() or  python3 -m unittest file_name

- typehints
    - declaring variable type, x: int
    - declaring function return type, function(x: 4) -> int

## Revision
1. NameError :if a variable does not exist

2. Conditional Operator x = 3 if 3 > 2 else 5

3. print("abc", end="\n")

4. Boolean Values: True/ False
Everything has a boolean value bool(0), bool(-1)

5. Conditional Opearators: and, or, not

6. Comparison Operators: ==, !=, <=, >=

   1 < 2 and 2 < 3 is same as 1 < 2 < 3

7. a is b # True i.e  a and b are the same object
   e.g a = [1,2,3] b=a
8. a == b # True i.e  a is equal to b in value

9. Comments: #, """ """, 

10. Numbers: int, float, /, // , 2 ** 3, enforce precedence (1 + 2) * 3

11. Strings, immutable, Slice, Step Size, String formatting, 
    upper, lower, count,  
    (Note: is None == None, almost does the same thing)

12. Sets , create a set, add element, discard element
    intersection, union, difference, symetric difference, discard/remove
    subset/superset <=, >=

13. Dictionary, keys should be immutable, keys can be strings, ints, floats , tuples
    Use x.get('key')
    Dictionary Expansion y = {"a": 10, **b}
    from collections import OrderedDict
    list(x.keys()), x.values(), x.items()

14. Lists are mutable
    l.append(5)
    l.pop()
    l.pop(0)
    l.insert(0,10)
    l.extend(b) 
    in operator in lists

15. tuples are good for unpacking
    a, b = 2, 3
    a, *b, c = [1,2,3,4,5]

16. Conditionals
    if , elif , else

17. Loops: for, while, break, continue
    using pass

18. function, documentation inside function
    arguments, and keyword arguments
    lambda expression
    map, filter, reduce, zip, zip + list, zip + list + dict
    enumerate, min, max
    function scope: L,E,G, B

19. List Comprehension
    LC with conditions (if / else)
    Generator Expression with LC
    Set Comprehension
    Dict Comprehension

20. Decorators
    Higher Order Function

21. Generator, yield keyword, lists /iterators, iter function on list , next function

22. File Operations
    using with to open files and perform read write and append

23. Exception Handling
    assert
    raise
    try/except/else/finally, print exception name
    custom excepotion
    

24. Classes
    - Class Variables
    - Instance Variables
    - Class Methods
    - Static Method
    - Regular Methods
    - Method Overloading
    - Private Vairables
    - Private Method
      - (How can private be not so private)
    - Magic Methods(str, del, len, )
    - Doc String Inside Classes/ Doc String Inside Methods
     
    
    Data Hiding 
     - abstraction
     - encapsulation

    Polymorphism
