#SYSTEM ADMINISTRATION USING PYTHON

##STRING
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


##Numbers
- int, float, typecasting
- + , - , **, /, ** , //
- from decimal import Decimal as d


##Boolean
- True False None

##Variables
- x = 1, x = '', x = '''   '''

##Lists
- mutable
- create a list []
- add [].append()
- add list1 + list2
- slice a list
- remove from a list using .remove(value)
- pop(), pop(index)
- new_list.sort() (In Place, returns None)
- reverse (In Place, returns None)


##Sets
- unordered collection of data
- hold unique values
- has  add method
- x = set()
- you can also convert a list into a set


##Tuples
- Create(10,)
- immutable
- Add new() = old() + (10,20)
- Unpack a tuple into multiple variables x,y,z = tupleSomething
- are like lists and preserver data integrity
- also used with print

##Dictionaries
- keys are ordered in python3
- Use Immutable Keys, don't use lists
- add keys, delete keys using del
- del dict[key], del dict
- dict.pop(key)
- Keys list(dict.keys())
- Values list(dict.values())
- Create dicts dict(key1=10, key2=20)
- Create dicts dict([('age',10),('name','bob')])

##Conditionals and Comparisons
- if / elif / else
- if condition: followed by indented next line
- > , >= , < , <=
- 2 in / not in [12,20]

##Loops
- while COND: pass
- continue in the while loop to continue with the  next iteration
- break to break the loop
- pass does nothing
- print(f'the total count is {count}')
- for var in list/tuple/dict.keys()
- iterate over a list of tuples for x,y in[(10,20),(30,40)]
- iterate over a dict for key,value in dict.items() 

##Logical Operations
- name = '' , not name
- you can use if not, we want something to execute when the value is false
- if one condition or other is true
- use or to set default values
- or will return the first truthy value or last value
- use and if both operations are true
- and will return the first value that is falsy or the last value

##UserInput
- input('Enter a value')
- age = int(input("Enter Age"))

##Functions
- def function_name():
- function can have return value


