"""https://t.me/pythonetc/233"""

"""Objects in python store their attributes in dictionaries that can be accessed by __dict__ magic attribute:"""


class A:
    pass


a = A()
a.x = 1
print(f"a.__dict__: {a.__dict__}")

"""By direct accessing it you can even create attributes that are not python identifiers
(which means you can't get them with a standard obj.attr syntax):"""

a.__dict__[' '] = 'empty'
print(f"a.__dict__: {a.__dict__}")
print(f"getattr(a, ' '): {getattr(a, ' ')}\n")


"""You can also ask python to store attributes directly in memory (like a simple C struct) using __slots__.
It will save some memory and some CPU cycles that are used for dictionary lookups."""


class Point:
    __slots__ = ['x', 'y']
p = Point()
p.x = 1
p.y = 2
print(f"p.x: {p.x}")
print(f"p.y: {p.y}\n")



"""There are some things you should remember while using slots.
First, you can't set any attributes that are not specified in __slots__.
Second, if some class is inherited from a class with slots, its __slots__ don't override parental __slots__
but are added to it:"""


class Parent:
    __slots__ = ['x']


class Child(Parent):
    __slots__ = ['y']


c = Child()
c.x = 1
c.y = 2
print(f"c.__slots__: {c.__slots__}")
print(f"Parent.__slots__: {Parent.__slots__}")
print(f"c.x = {c.x}")
print(f"c.y = {c.y}\n")

try:
    print(f"c.__dict__: {c.__dict__}")
except AttributeError as e:
    print(repr(e))


"""Third, you can't inherit from two different classes with nonempty __slots__, even if they are identical.
You can get more information from this excellent Stack Overflow answer
(https://stackoverflow.com/a/28059785/1102638).

Remember, that slots is meant for optimization, not for constraining attributes."""
