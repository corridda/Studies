"""abs(x)"""
# https://www.programiz.com/python-programming/methods/built-in/abs

"""Return the absolute value of a number. The argument may be an integer or a floating point number.
If the argument is a complex number, its magnitude is returned."""

print(f"abs(1): {abs(1)}")
print(f"abs(-1): {abs(-1)}")
print(f"abs(-1.5): {abs(-1.5)}\n")


# Get magnitude of a complex number
"""Модуль комплексного числа {\displaystyle z=x+iy} z=x+iy обозначается |z| и определяется выражением
|z| = sqrt(x**2 + y**2)"""

print(f"abs(1+2j): {abs(1+2j)}")
print(f"abs(-1+2j): {abs(-1+2j)}")
print(f"abs(-1-2j): {abs(-1-2j)}")
complex = (3 - 4j)
print('Magnitude of 3-4j is:', abs(complex))
