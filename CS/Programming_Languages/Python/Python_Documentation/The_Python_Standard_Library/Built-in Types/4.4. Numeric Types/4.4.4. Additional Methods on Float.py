"""Additional Methods on Float"""

"""float also has the following additional methods.

float.as_integer_ratio()
    Return a pair of integers whose ratio is exactly equal to the original float and with a positive denominator.
    Raises OverflowError on infinities and a ValueError on NaNs.
float.is_integer()
    Return True if the float instance is finite with integral value, and False otherwise
"""
print(f"(-2.0).is_integer(): {(-2.0).is_integer()}")
print(f"(3.2).is_integer(): {(3.2).is_integer()}\n")


"""float.hex()
    Return a representation of a floating-point number as a hexadecimal string.
classmethod float.fromhex(s)
    Class method to return the float represented by a hexadecimal string s.
"""
# For example, the hexadecimal string 0x3.a7p10 represents the floating-point number
# (3 + 10./16 + 7./16**2) * 2.0**10, or 3740.0:
print(f"float.fromhex('0x3.a7p10'): {float.fromhex('0x3.a7p10')}")

# Applying the reverse conversion to 3740.0 gives a different hexadecimal string representing the same number:
print(f"float.hex(3740): {float.hex(3740.0)}")

