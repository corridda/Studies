"""The decimal module offers a Decimal datatype for decimal floating point arithmetic."""

from decimal import *

print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(round(.70 * 1.05, 2), '\n')

# Exact representation enables the Decimal class to perform modulo calculations and equality tests
# that are unsuitable for binary floating point:
print(Decimal('1.00') % Decimal('.10'))
print(1.00 % 0.10, '\n')

print(f"sum([Decimal('0.1')] * 10): {sum([Decimal('0.1')] * 10)}")
print(sum([Decimal('0.1')] * 10) == Decimal('1.0'))
print(f"sum([0.1] * 10): {sum([0.1] * 10)}")
print(sum([0.1] * 10) == 1.0, '\n')

# The decimal module provides arithmetic with as much precision as needed:
getcontext().prec = 36
print(f"Decimal(1) / Decimal(7): {Decimal(1) / Decimal(7)}")
print(f"(Decimal(1) / Decimal(7)).__sizeof__(): {(Decimal(1) / Decimal(7)).__sizeof__()}\n")

print(f"1 / 7: {1 / 7}")
print(f"(1 / 7).__sizeof__(): {(1 / 7).__sizeof__()}\n")

getcontext().prec = 17
print(f"Decimal(1) / Decimal(7): {Decimal(1) / Decimal(7)}")
print(f"(Decimal(1) / Decimal(7)).__sizeof__(): {(Decimal(1) / Decimal(7)).__sizeof__()}")
