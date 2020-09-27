"""pow(x, y[, z])"""
# https://www.programiz.com/python-programming/methods/built-in/pow

"""Return x to the power y; if z is present, return x to the power y, modulo z (computed more efficiently
than pow(x, y) % z). The two-argument form pow(x, y) is equivalent to using the power operator: x ** y.

The arguments must have numeric types. With mixed operand types, the coercion rules
for binary arithmetic operators apply. For int operands, the result has the same type as the operands
(after coercion) unless the second argument is negative;
in that case, all arguments are converted to float and a float result is delivered.
For example, 10 ** 2 returns 100, but 10 ** -2 returns 0.unit_01. If the second argument is negative,
the third argument must be omitted. If z is present, x and y must be of integer types, and y must be non-negative.
"""

# Example 1: How pow() works in Python?

# positive x, positive y (x**y)
print(f"pow(2, 2): {pow(2, 2)}")

# negative x, positive y
print(f"pow(-2, 2): {pow(-2, 2)}")

# positive x, negative y (x**-y)
print(f"pow(2, -2): {pow(2, -2)}")

# negative x, negative y
print(f"pow(-2, -2): {pow(-2, -2)}\n")



# Example 2: pow() with three arguments (x**y) % z

x = 7
y = 2
z = 5

# Here, 7 is powered by 2 (7**2) which equals 49. Then, 49 modulus 5 (49 % 5) equals 4.
print(f"pow({x}, {y}, {z}): {pow(x, y, z)}")