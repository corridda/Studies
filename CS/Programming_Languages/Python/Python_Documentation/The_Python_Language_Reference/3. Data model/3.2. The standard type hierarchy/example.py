# None
a = None
b = None
print(f"a: {a}")
print(f"a is b: {a is b}")
print(f"type(a): {type(a)}")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}\n")

# NotImplemented
a = NotImplemented
b = NotImplemented
print(f"a: {a}")
print(f"a is b: {a is b}")
print(f"type(a): {type(a)}")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}\n")

# Ellipsis
a = Ellipsis
b = ...
print(f"a: {a}")
print(f"a is b: {a is b}")
print(f"type(a): {type(a)}")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}\n")


# numbers.Complex
a = 1-2j
print(f"a: {a}")
print(f"a.real: {a.real}")
print(f"a.imag: {a.imag}")
print(f"type(a): {type(a)}")
print(f"id(a): {id(a)}\n")



"""Sequences"""

# Immutable sequences

# Strings
a = 'This is a string.'
print(f"a: {a}")
print(f"type(a): {type(a)}")
print(f"a[0]: {a[0]}")
print(f"a[0:2]: {a[0:2]}")

# The built-in function ord() converts a code point from its string form to an integer in the range 0 - 10FFFF;
unicode = [ord(x) for x in a]
print(f"unicode: {unicode}")

# chr() converts an integer in the range 0 - 10FFFF to the corresponding length 1 string object.
print(f"''.join([chr(x) for x in unicode]): {''.join([chr(x) for x in unicode])}")

# str.encode() can be used to convert a str to bytes using the given text encoding
print(f"str.encode(a): {str.encode(a)}")
print(f"type(str.encode(a)): {type(str.encode(a))}")

# ... and bytes.decode() can be used to achieve the opposite:
print(f"bytes.decode(str.encode(a)): {bytes.decode(str.encode(a))}")
print(f"type(bytes.decode(str.encode(a))): {type(bytes.decode(str.encode(a)))}\n")


# Tuples
a = (1, 2)
print(f"a: {a}")
print(f"type(a): {type(a)}")

# An empty tuple can be formed by an empty pair of parentheses.
b = ()
print(f"b: {b}")
print(f"type(b): {type(b)}")

# A tuple of one item (a ‘singleton’) can be formed by affixing a comma to an expression:
c = (10,)
print(f"c: {c}")
print(f"type(c): {type(c)}")


# Bytes
# Bytes literals (like b'abc') and the built-in bytes() constructor can be used to create bytes objects.
a = b'abc'
print(f"a: {a}")
print(f"type(a): {type(a)}")
b = bytes(b'cde')
print(f"b: {b}")
print(f"type(b): {type(b)}\n")




# Mutable sequences

# Lists
a = []
print(f"a: {a}")
print(f"type(a): {type(a)}\n")


# Byte Arrays
# A bytearray object is a mutable array. They are created by the built-in bytearray() constructor.
a = bytearray(b'This is a bytearray.')
print(f"a: {a}")
print(f"type(a): {type(a)}")
print(f"a[0:5]: {a[0:5]}")
print(f"len(a): {len(a)}\n")




"""Set types"""

# Sets
a = set()
print(f"a: {a}")
print(f"type(a): {type(a)}")
a.add(1)
print(f"a: {a}")

# If two numbers compare equal (e.g., 1 and 1.0), only one of them can be contained in a set.
a.add(1.0)
print(f"a: {a}\n")


# Frozen sets
# These represent an immutable set.
a = frozenset([1, 2, 3])
print(f"a: {a}")
print(f"type(a): {type(a)}")
try:
    a.add(4)
except AttributeError as e:
    print(repr(e))

# As a frozenset is immutable and hashable, it can be used again as an element of another set, or as a dictionary key.
b = {}
b[a] = 'frozenset'
print(f"b: {b}\n")




"""Mappings"""

# Dictionaries
a = {1: 'one', 2: 'two', 3: 'three'}
print(f"a: {a}")
print(f"type(a): {type(a)}")
print(f"len(a): {len(a)}")
print(f"a[3]: {a[3]}\n")




"""Callable types"""

# User-defined functions
def show_example():
    pass
print(f"type(show_example): {type(show_example)}")


# Instance methods
class A:
    class B:
        def show_special_attributes(self, default_a:int = 1, default_b:int = 2) -> None:
            """Show the function's special attributes."""

            print('Inside the function.')

B = A().B()
f = B.show_special_attributes
print(f"type(f): {type(f)}")
print(f"f.__doc__: {f.__doc__}")
print(f"f.__name__: {f.__name__}")
print(f"f.__qualname__: {f.__qualname__}")
print(f"f.__module__: {f.__module__}")
print(f"f.__defaults__: {f.__defaults__}")
print(f"f.__code__: {f.__code__}")
print(f"f.__globals__: {f.__globals__}")
print(f"f.__dict__: {f.__dict__}")
print(f"f.__closure__: {f.__closure__}")
print(f"f.__annotations__: {f.__annotations__}")
print(f"f.__kwdefaults__: {f.__kwdefaults__}")





















