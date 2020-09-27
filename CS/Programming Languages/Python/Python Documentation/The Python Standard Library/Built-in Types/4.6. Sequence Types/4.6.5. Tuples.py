"""Tuples"""

"""class tuple([iterable])
Tuples may be constructed in a number of ways:
    •Using a pair of parentheses to denote the empty tuple: ()
    •Using a trailing comma for a singleton tuple: a, or (a,)
    •Separating items with commas: a, b, c or (a, b, c)
    •Using the tuple() built-in: tuple() or tuple(iterable)
"""

print(f"('a','b','c') == tuple(['a','b','c']) == tuple('abc'): "
      f"{('a', 'b', 'c') == tuple(['a', 'b', 'c']) == tuple('abc')}")
print(f"empty tuple: {tuple()}")
print(f"tuple of one element: {(1,)}\n")

"""The parentheses are optional, except in the empty tuple case, or when they are needed
to avoid syntactic ambiguity. """
a = 1, 2, 3
print(f"a: {a}")
print(f"type(a): {type(a)}\n")

"""For heterogeneous collections of data where access by name is clearer than access by index,
collections.namedtuple() may be a more appropriate choice than a simple tuple object."""
