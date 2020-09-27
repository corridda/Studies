"""https://t.me/pythonetc/234"""

from pprint import pprint

"""
The biggest drawback of objects with __slots__ is that they can't dynamically have arbitrary attributes.
However, you can mix the __slots__ approach with the regular __dict__ one.

To enable dynamic assignment for the object just put '__dict__' into __slots__:"""

class A:
    __slots__ = ('a', 'b', '__dict__')

A().x = 3
print(f"A.__slots__: {A.__slots__}")
print('A.__dict__:')
pprint(f"{A.__dict__}", compact=True)

"""Also, mind that inherited classes automatically has __dict__ unless empty __slots__ is explicitly specified:"""

class A:
    __slots__ = ('a', 'b')

class B(A):
    pass

B().x = 3
