"""Hashing of numeric types"""

import sys, math
from fractions import Fraction

"""The value of P is made available to python as the modulus attribute of sys.hash_info."""
print(sys.hash_info, '\n')


def hash_fraction(m, n):
    """Compute the hash of a rational number m / n.

    Assumes m and n are integers, with n positive.
    Equivalent to hash(fractions.Fraction(m, n)).

    """
    P = sys.hash_info.modulus
    # Remove common factors of P.  (Unnecessary if m and n already coprime.)
    while m % P == n % P == 0:
        m, n = m // P, n // P

    if n % P == 0:
        hash_value = sys.hash_info.inf
    else:
        # Fermat's Little Theorem: pow(n, P-1, P) is 1, so
        # pow(n, P-2, P) gives the inverse of n modulo P.
        hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
    if m < 0:
        hash_value = -hash_value
    if hash_value == -1:
        hash_value = -2
    return hash_value

def hash_float(x):
    """Compute the hash of a float x."""

    if math.isnan(x):
        return sys.hash_info.nan
    elif math.isinf(x):
        return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
    else:
        return hash_fraction(*x.as_integer_ratio())

def hash_complex(z):
    """Compute the hash of a complex number z."""

    hash_value = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
    # do a signed reduction modulo 2**sys.hash_info.width
    M = 2**(sys.hash_info.width - 1)
    hash_value = (hash_value & (M - 1)) - (hash_value & M)
    if hash_value == -1:
        hash_value = -2
    return hash_value

print(f"hash_fraction(3, 7): {hash_fraction(3, 7)}")
print(f"Fraction(3,7).__hash__(): {Fraction(3,7).__hash__()}")
print(f"hash(Fraction(3,7)): {hash(Fraction(3,7))}\n")
print(f"hash_float(3.5): {hash_float(3.5)}")
print(f"(3.5).__hash__(): {(3.5).__hash__()}\n")
print(f"hash_complex(5+2j): {hash_complex(5+2j)}")
print(f"(5+2j).__hash__(): {(5+2j).__hash__()}\n")