#!/usr/bin/python3.9
__author__ = 'Igor Vasilev'

import math


def get_multiplicative_inverse(x: int, m: int):
    """Returns y such that x * y == 1 modulo m, or 0 if no such y exists."""
    if x == 0:
        return 0
    elif math.gcd(x, m) == 1:
        return pow(x, -1, m)
    else:
        return 0
