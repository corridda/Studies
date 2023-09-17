"""Numeric Types — int, float, complex"""

from sys import float_info
from pprint import pprint


"""Information about the precision and internal representation of floating point numbers
for the machine on which your program is running is available in sys.float_info."""
print('float_info:')
pprint(f"{float_info}")
print()


"""Complex numbers have a real and imaginary part, which are each a floating point number.
To extract these parts from a complex number z, use z.real and z.imag."""
z = 5+2j
print(f"z:{z}\nz.real: {z.real}\nz.imag: {z.imag}\n")


"""python fully supports mixed arithmetic: when a binary arithmetic operator has operands of different numeric types,
the operand with the “narrower” type is widened to that of the other, where integer is narrower than floating point,
which is narrower than complex."""
print(f"int(10) == float(10.0): {int(10) == float(10.0)}")
print(f"float(10.0) == complex(10, 0j): {float(10.0) == complex(10, 0j)}\n")


