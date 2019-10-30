#!/usr/bin/env python3


from collections import deque
import itertools

test_d = deque()
test_d.append('a')
test_d.append('b')
test_d.appendleft('z')
print(test_d)
print(list(itertools.islice(test_d, 0, 3)))

test_d.pop()
test_d.popleft()
print(test_d)

dq2 = deque([], maxlen=3)
[ dq2.append(i) for i in range(6) ]
print(dq2)
