"""class object"""
# https://www.programiz.com/python-programming/methods/built-in/object

"""Return a new featureless object. object is a base for all classes.
It has the methods that are common to all instances of Python classes. This function does not accept any arguments.
Note: object does not have a __dict__, so you can’t assign arbitrary attributes to an instance of the object class.
"""

# Example: How object() works?
test = object()
print(f"type(test): {type(test)}")
print(f"dir(test): {dir(test)}")