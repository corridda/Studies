"""class float([x])"""
# https://www.programiz.com/python-programming/methods/built-in/float

"""Return a floating point number constructed from a number or string x."""

print(f"float(): {float()}")
print(f"float(10.5): {float(10.5)}")
s = '    -2.5\n'
print(f"float('    -2.5'): {float(s)}")
print(f"float('NaN'): {float('NaN')}")
print(f"float('Infinity'): {float('Infinity')}")
print(f"float('-Infinity'): {float('-Infinity')}")
print(f"float('1e-003'): {float('1e-003')}")
print(f"float(1_000_000): {float(1_000_000)}")

try:
    print(f"float('abc'): {float('abc')}")
except ValueError as e:
    print(repr(e))

