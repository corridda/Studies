"""Memory Views"""

import array
from ctypes import BigEndianStructure, c_long
import struct

"""class memoryview(obj)
    Create a memoryview that references obj. obj must support the buffer protocol.
    Built-in objects that support the buffer protocol include bytes and bytearray."""

"""A memoryview supports slicing and indexing to expose its data. One-dimensional slicing will result in a subview:"""
v = memoryview(b'abcefg')
print(f"v[1]: {v[1]}")
print(f"chr(v[1]: {chr(v[1])}")
print(f"v[-1]: {v[-1]}")
print(f"v[1:4]: {v[1:4]}")
print(f"bytes(v[1:4]): {bytes(v[1:4])}\n")


# Here is an example with a non-byte format:
a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
m = memoryview(a)
print(f"m[0]: {m[0]}")
print(f"m[-1]: {m[-1]}")
print(f"m[::2].tolist(): {m[::2].tolist()}\n")


"""If the underlying object is writable, the memoryview supports one-dimensional slice assignment.
Resizing is not allowed:"""
data = bytearray(b'abcefg')
v = memoryview(data)
print(f"v.readonly: {v.readonly}")
v[0] = ord(b'z')
print(f"data: {data}")
v[1:4] = b'123'
print(f"data: {data}")
try:
    v[2:3] = b'spam'
except ValueError as e:
    print(repr(e))
v[2:6] = b'spam'
print(f"data: {data}\n")


"""One-dimensional memoryviews of hashable (read-only) types with formats ‘B’, ‘b’ or ‘c’ are also hashable.
The hash is defined as hash(m) == hash(m.tobytes()):"""
v = memoryview(b'abcefg')
print(f"hash(v) == hash(b'abcefg'): {hash(v) == hash(b'abcefg')}")
print(f"hash(v[2:4]) == hash(b'ce'): {hash(v[2:4]) == hash(b'ce')}")
print(f"hash(v[::-2]) == hash(b'abcefg'[::-2]): {hash(v[::-2]) == hash(b'abcefg'[::-2])}\n")




"""memoryview has several methods:"""


# __eq__(exporter)
"""For the subset of struct format strings currently supported by tolist(), v and w are equal
if v.tolist() == w.tolist():"""
a = array.array('I', [1, 2, 3, 4, 5])
b = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
c = array.array('b', [5, 3, 1])
x = memoryview(a)
y = memoryview(b)
print(f"x == a == y == b: {x == a == y == b}")
print(f"x.tolist() == a.tolist() == y.tolist() == b.tolist(): "
      f"{x.tolist() == a.tolist() == y.tolist() == b.tolist()}")
z = y[::-2]
print(f"z == c: {z == c}")
print(f"z.tolist() == c.tolist(): {z.tolist() == c.tolist()}\n")

"""If either format string is not supported by the struct module, then the objects will always compare
as unequal (even if the format strings and buffer contents are identical):
(Note that, as with floating point numbers, v is w does not imply v == w for memoryview objects.)"""
class BEPoint(BigEndianStructure):
    _fields_ = [("x", c_long), ("y", c_long)]

point = BEPoint(100, 200)
a = memoryview(point)
b = memoryview(point)
print(f"a == point: {a == point}")
print(f"a == b: {a == b}\n")



# tobytes()
m = memoryview(b"abc")
print(f"m.tobytes(): {m.tobytes()}")
print(f"bytes(m): {bytes(m)}\n")



# hex()
print(f"m.hex(): {m.hex()}\n")



# tolist()
print(f"m.tolist(): {m.tolist()}")
a = array.array('d', [1.1, 2.2, 3.3])
m = memoryview(a)
print(f"m.tolist(): {m.tolist()}\n")



# release()
m = memoryview(b'abc')
"""After this method has been called, any further operation on the view raises a ValueError
(except release() itself which can be called multiple times):"""
m.release()
try:
    print(f"m[0]: {m[0]}\n")
except ValueError as e:
    print(repr(e))

"""The context management protocol can be used for a similar effect, using the with statement:"""
with memoryview(b'abc') as m:
    print(f"m[0]: {m[0]}")
try:
    print(f"m[0]: {m[0]}\n")
except ValueError as e:
    print(repr(e), '\n')



# cast(format[, shape])
# Cast 1D/long to 1D/unsigned bytes:
a = array.array('l', [1,2,3])
x = memoryview(a)
print(f"x.format: {x.format}")
print(f"x.itemsize: {x.itemsize}")
print(f"len(x): {len(x)}")
print(f"x.nbytes: {x.nbytes}")
y = x.cast('B')
print(f"y.format: {y.format}")
print(f"y.itemsize: {y.itemsize}")
print(f"len(y): {len(y)}")
print(f"y.nbytes: {y.nbytes}")
print(f"y.tolist(): {y.tolist()}\n")

# Cast 1D/unsigned bytes to 1D/char:
b = bytearray(b'zyz')
x = memoryview(b)
try:
    x[0] = b'a'
except TypeError as e:
    print(repr(e))
y = x.cast('c')
y[0] = b'a'
print(f"b: {b}\n")

# Cast 1D/bytes to 3D/ints to 1D/signed char:
buf = struct.pack("i"*12, *list(range(12)))
x = memoryview(buf)
y = x.cast('i', shape=[2,2,3])
print(f"y.tolist(): {y.tolist()}")
print(f"y.format: {y.format}")
print(f"y.itemsize: {y.itemsize}")
print(f"len(y): {len(y)}")
print(f"y.nbytes: {y.nbytes}")
z = y.cast('b')
print(f"z.format: {z.format}")
print(f"z.itemsize: {z.itemsize}")
print(f"len(z): {len(z)}")
print(f"z.nbytes: {z.nbytes}\n")

# Cast 1D/unsigned char to 2D/unsigned long:
buf = struct.pack("L"*6, *list(range(6)))
x = memoryview(buf)
y = x.cast('L', shape=[2,3])
print(f"len(y): {len(y)}")
print(f"y.nbytes: {y.nbytes}")
print(f"y.tolist(): {y.tolist()}\n")



"""There are also several readonly attributes available:"""

# obj
b  = bytearray(b'xyz')
m = memoryview(b)
print(f"m.obj is b: {m.obj is b}\n")

# nbytes
a = array.array('i', [1,2,3,4,5])
m = memoryview(a)
print(f"len(m): {len(m)}")
print(f"m.nbytes: {m.nbytes}")
y = m[::2]
print(f"len(y): {len(y)}")
print(f"y.nbytes: {y.nbytes}")
print(f"y.tolist(): {y.tolist()}\n")
# Multi-dimensional arrays:
buf = struct.pack("d"*12, *[1.5*x for x in range(12)])
x = memoryview(buf)
y = x.cast('d', shape=[3,4])
print(f"y.tolist(): {y.tolist()}")
print(f"len(y): {len(y)}")
print(f"y.nbytes: {y.nbytes}\n")

# readonly
print(f"y.readonly: {y.readonly}\n")

# format
print(f"y.format: {y.format}\n")

# itemsize
m = memoryview(array.array('H', [32000, 32001, 32002]))
print(f"m.itemsize: {m.itemsize}")
print(f"m[0]: {m[0]}")
print(f"struct.calcsize('H') == m.itemsize: {struct.calcsize('H') == m.itemsize}\n")

# ndim
print(f"y.tolist(): {y.tolist()}")
print(f"y.ndim: {y.ndim}")

# shape
print(f"y.shape: {y.shape}")

# strides
print(f"y.strides: {y.strides}")

# suboffsets
print(f"y.suboffsets: {y.suboffsets}")

# c_contiguous
print(f"y.c_contiguous: {y.c_contiguous}")

# f_contiguous
print(f"y.f_contiguous: {y.f_contiguous}")

# contiguous
print(f"y.contiguous: {y.contiguous}")
