"""Comparisons"""

from dataclasses import dataclass


"""Comparisons can be chained arbitrarily; for example, x < y <= z is equivalent to x < y and y <= z,
except that y is evaluated only once (but in both cases z is not evaluated at all when x < y is found to be false)."""

x = 3
y = 2
# z = 2

if not x < y <= z:
    print(f"'x <= z' wasn't evaluated.\n")



"""Objects of different types, except different numeric types, never compare equal."""

class A:
    pass

class B:
    pass

if A() != B():
    print(f"'A()' not equal 'B()'\n")



"""Non-identical instances of a class normally compare as non-equal unless the class defines the __eq__() method."""

@dataclass(order=True)
class C:
    c1: int

print(f"A() == A(): {A() == A()}")
print(f"C(1) == C(1): {C(1) == C(1)}")
print(f"C(1) == C(2): {C(1) == C(2)}\n")



"""Instances of a class cannot be ordered with respect to other instances of the same class,
or other types of object, unless the class defines enough of the methods __lt__(), __le__(), __gt__(), and __ge__()
(in general, __lt__() and __eq__() are sufficient, if you want the conventional meanings
of the comparison operators)."""

class D:
    def __init__(self, d):
        self.d = d
    def __repr__(self):
        return str(self.d)

list_of_D = [D(3), D(2), D(1)]
try:
    print(sorted(list_of_D))
except TypeError as e:
    print(repr(e))
print()

list_of_C = [C(3), C(2), C(1)]
try:
    print(sorted(list_of_C))
except TypeError as e:
    print(repr(e))
print()



"""The behavior of the 'is' and 'is not' operators cannot be customized; also they can be applied to any two objects
and never raise an exception."""
if C(1) is not None:
    print("C(1) is not None")
else:
    print("C(1) is None")
print()



