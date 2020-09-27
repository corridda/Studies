"""https://t.me/pythonetc/431"""

"""Dictionaries that are used for storing object attributes are not the same that you create with dict
though they look exactly the same:"""

from sys import getsizeof

class A:
    pass

a = dict()
b = A().__dict__

print(f"type(a): {type(a)}")
print(f"type(b): {type(b)}")
print(f"a: {a}")
print(f"b: {b}")
print(f"getsizeof(a): {getsizeof(a)}")
print(f"getsizeof(b): {getsizeof(b)}")

"""For reduction in memory used, dictionaries for __dict__ are implemented differently.
They are sharing keys across all instances of A. Mind, however, that b is not actually smaller than a,
it’s just how getsizeof works.

Read all the details here:
https://www.python.org/dev/peps/pep-0412/"""