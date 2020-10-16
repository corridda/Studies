"""Bitwise Operations on Integer Types"""

"""Bitwise operations only make sense for integers. The result of bitwise operations is calculated
as though carried out in two’s complement with an infinite number of sign bits."""

# x | y bitwise or of x and y
x = 101
y = 41
print(f"x = {x}; y = {y}")
print(f"bin(x): 0b{x:>07b}")
print(f"bin(y): 0b{y:>07b}")
print(f"bin(x | y): 0b{x | y:>07b}\n")


# x ^ y bitwise exclusive or of x and y
x = 101
y = 41
print(f"x = {x}; y = {y}")
print(f"bin(x): 0b{x:>07b}")
print(f"bin(y): 0b{y:>07b}")
print(f"bin(x ^ y): 0b{x ^ y:>07b}\n")


# x & y bitwise and of x and y
x = 101
y = 41
print(f"x = {x}; y = {y}")
print(f"bin(x): 0b{x:>07b}")
print(f"bin(y): 0b{y:>07b}")
print(f"bin(x & y): 0b{x & y:>07b}\n")


# x << n x shifted left by n bits
x = 101
print(f"x = {x}")
print(f"bin(x): 0b{x:>07b}")
print(f"bin(x << 1): 0b{x << 1:>07b}\n")


# x >> n x shifted right by n bits
x = 101
print(f"x = {x}")
print(f"bin(x): 0b{x:>07b}")
print(f"bin(x >> 1): 0b{x >> 1:>07b}\n")


# ~x the bits of x inverted
x = -61
print(f"x = {x}")
print(f"bin(x): {x:>07b}")
print(f"~x = {~x}")
print(f"bin(~x): {~x:>07b}\n")