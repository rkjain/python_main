'''
Big O Notation:
  - Algorithm Complexity, Memory Consumption

Sorting Algorithms:
  - Bubble Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort
  - Radix Sort
  - Heap Sort
  - Binary Tree Sort

Advanced Algorithms:
  - Dijkstras Algorithm
  - Dynamic Programming
  - String Matching

Graph Algorithms:
  - Depth First Search
  - Breadth First Search
  - Maximum Flow

Data Structures:
  - Stack, Queue, Linked List, Heap
  - Hash Function, Hash Table, Hash Set, Hash Map
  - Binary Tree, Prefix Tree, Quad Tree

Advanced:
  - Disjoint Set
  - Linear Program
  - Linear Algebra:
    - Vector, Inner / Cross Product
    - Matrix Manipulation, Single Value Decomposition, Orthogonalizaition
  - Source Coding Algorithms: Run Length Coding, Huffman Coding

Reference:
  -  Introduction to Algorithms, Cormen

Solving Daunting Technical Problems:
  - Solve Trival Cases First 0,1 in Fib Series
  - Brute Force Algorithms First (Moving Average With window size K)

Coding Style:
  - consistency
  - readability over code length (Serialize A Binary Tree)
  - Python:
    - https://github.com/google/styleguide/blob/gh-pages/pyguide.md

Sort:
  - Find More on Inbuilt Sort functions in python
  - Bubble Sort
  - Merge Sort
  - Heap Sort
  - Binary Tree Sort
  - Quick Sort
  - Inbuilt Sort In Python Using Sorted, with key as a lambda function

Trees:
  - Binary Search Trees
    - Average Time Complexity, Space
  - Binary Tree Traversal
    - InOrder
    - PreOrder
    - PostOrder
  - Serialization/Deserialization of Binary Tree

Traversal:
  - DFS (InOrder, PreOrder, PostOrder)
  - BFS (Level), Use a Queue
  - Count # of Islands (DFS)
  - Find Deepest Node in BST (BFS)

String Manipulation:
  - String Matching
    - Find Occurences Of A Pattern In Text (S)
    - Naive Algorithms: O(nm)
    - Rabin Karp Algorithm O(n + m)
  - String Search
    - Find Longest Substring With 2 Unique Characters
    - Linear Search Algorithm
    - Find Longest Word Containing Input Characters

Dynamic Programming:
  - Longest Increasing Subsequence (DAG)
  - Fibo Number, Memoization
  - Low Cost Graph from A to N

Cocurrency:
  - Concurrency, Parallelism, Multithreading
  - Shared Resources:
    - Critical Section, Mutex, Semaphore
  - Busy Waiting
    - Avoid by using Semaphore, and Events

Design Question:
  - How to implement a webbrowser ?


'''



def find_vowel(glist):
    vs = {"a","e","i","o","u"}
    mlist = list(glist)
    for elem in mlist:
        if elem in vs:
            return elem

def int_vowels(my_string):
    sm_string = list(my_string)
    get_first_elem = find_vowel(sm_string)
    get_first_elem_index = sm_string.index(get_first_elem)
    get_second_elem = find_vowel(sm_string[get_first_elem_index + 1:])
    get_second_elem_index = sm_string.index(get_second_elem)
    sm_string[get_first_elem_index], sm_string[get_second_elem_index] = sm_string[get_second_elem_index], sm_string[get_first_elem_index]
    return "".join(sm_string)

print(int_vowels('apple'))
print(int_vowels('friend'))