"""repr(object)"""
# https://www.programiz.com/python-programming/methods/built-in/repr

"""Return a string containing a printable representation of an object.
For many types, this function makes an attempt to return a string that would yield an object with the same value
when passed to eval(), otherwise the representation is a string enclosed in angle brackets
that contains the name of the type of the object together with additional information
often including the name and address of the object. A class can control what this function returns
for its instances by defining a __repr__() method."""


# Example 1: How repr() works in python?
"""It is important to that 'foo' is a string so it's represented by the single quotes.
'foo' without the quotes would assign var to foo variable."""
var = 'foo'
print(f"repr(var): {repr(var)}")



# Example 2: Implement __repr__() for custom objects
"""Internally, repr() method calls __repr__() method of the given object.
You can easily implement/override the __repr__() method to use your own value for the repr() output."""
class Person:
    name = 'Adam'

    def __repr__(self):
        return repr(self.name)

print(f"repr(Person()): {repr(Person())}")

