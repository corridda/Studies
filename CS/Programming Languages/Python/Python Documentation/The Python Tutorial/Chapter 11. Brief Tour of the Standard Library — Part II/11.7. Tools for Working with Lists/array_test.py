"""The array module provides an array() object that is like a list that stores only homogeneous data
and stores it more compactly"""

import sys
from array import array

a = [1,2, "three"]
print(a, '\n')

a = array('H', [4000, 10, 700, 22222])
print(type(a))
print(a)
print(sum(a))
print(a[1:3])
print(f'a.count(700): {a.count(700)}')
print(f'a.count(1): {a.count(1)}')
print()

b = array('I')
print(f'b: {b}')
b.append(0)
print(f'b: {b}')

# It's not acceptable to add negative number
try:
    b.append(-1)
except OverflowError as e:
    print(f'b.append(-1): {repr(e)}')
try:
    b.append(2**32)
except OverflowError as e:
    print(f'b.append(2**32): {repr(e)}')
try:
    b.append(2**32 - 1)
except OverflowError as e:
    print(f'b.append(2**32 - 1): {repr(e)}')
print(f'b: {b}\n')

a = []
print(f'type(a): {type(a)}')
print(f'a.__sizeof__(): {a.__sizeof__()}')
a.append(1)
print(f'a.__sizeof__(): {a.__sizeof__()}')
a.append(2)
print(f'a.__sizeof__(): {a.__sizeof__()}')
a.append(3)
print(f'a.__sizeof__(): {a.__sizeof__()}')
a.extend([4,5,6,7,8,9,10])
print(f'a.__sizeof__(): {a.__sizeof__()}\n')

a = array('I')
print(f'type(a): {type(a)}')
print(f'a.__sizeof__(): {a.__sizeof__()}')
a.append(1)
print(f'a.__sizeof__(): {a.__sizeof__()}')
a.append(2)
print(f'a.__sizeof__(): {a.__sizeof__()}')
a.append(3)
print(f'a.__sizeof__(): {a.__sizeof__()}')
a.extend([4,5,6,7,8,9,10])
print(f'a.__sizeof__(): {a.__sizeof__()}\n')