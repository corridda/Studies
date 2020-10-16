"""Truth Value Testing"""

from decimal import Decimal
from fractions import Fraction


"""By default, an object is considered true unless its class defines either a __bool__() method that returns False
or a __len__() method that returns zero, when called with the object."""

class A:
    pass

class B:
    def __bool__(self):
        return False

class C:
    def __len__(self):
        return 0

if A():
    print("A() cosidered true")
if not B():
    print("B() cosidered false")
if not C():
    print(f"C() cosidered false\n")


"""Here are most of the built-in objects considered false:
    •constants defined to be false: None and False.
    •zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
    •empty sequences and collections: '', (), [], {}, set(), range(0)
"""

print(f"False == False: {False == False}")
print(f"None == False: {None == False}")
if None:
    print('None == True')
elif not None:
    print('None considered false')
print()

print(f"0 == 0.0 == 0j == Decimal(0) == Fraction(0, 1) == False: "
      f"{0 == 0.0 == 0j == Decimal(0) == Fraction(0, 1) == False}\n")

if not '' and not [] and not {} and not set() and not range(0):
    print("'', (), [], {}, set(), range(0) considered false.")