#!/usr/bin/env python3
from heapq import heapify, heappush, heappop
from heapq import nlargest, nsmallest

"""
    - For a heap, for any index k
      left child is at 2k + 1
      and right child is at 2k + 2

    - Starting max_index / 2 all children are leaf
      nodes
"""

## Min Heap

convert_heap = [19,20, -1,2,3,4,5,6,7,8]
heapify(convert_heap)
print(convert_heap)

### Get 3 smallest numbers

### Create a min heap
min_heap = []
for i in range(1, 10):
    heappush(min_heap, i)

## Get Top element from the heap
print(min_heap[0])

## Pop few elements starting
while min_heap:
    print("Next Top: ", min_heap[0])
    print(heappop(min_heap))

### Max Heap
max_heap = [1,2,4,5,0,-23,-45,90,100]
vmax_heap = [-x for x in max_heap]

heapify(vmax_heap)

# Get Top 5
print("Top 5: ", [-x for x in nsmallest(5, vmax_heap)] )

for i in range(5):
    print("Head: ", -vmax_heap[0])
    print("Top: ", -heappop(vmax_heap))
