"""
    class type(object)
    class type(name, bases, dict)
"""
# https://www.programiz.com/python-programming/methods/built-in/type

"""
With one argument, return the type of an object. The return value is a type object and generally the same object
as returned by object.__class__.

The isinstance() built-in function is recommended for testing the type of an object,
because it takes subclasses into account.

With three arguments, return a new type object. This is essentially a dynamic form of the class statement.
The name string is the class name and becomes the __name__ attribute; the bases tuple itemizes
the base classes and becomes the __bases__ attribute; and the dict dictionary is the namespace
containing definitions for class body and is copied to a standard dictionary to become the __dict__ attribute.
For example, the following two statements create identical type objects:

>>> class X:
...     a = 1
...
>>> X = type('X', (object,), dict(a=1))

"""


"""type() With a Single Object Parameter
If the single object argument is passed to type(), it returns type of the given object."""

# Example 1: How to get type of an object?

numberList = [1, 2]
print(f"type(numberList): {type(numberList)}")

numberDict = {1: 'one', 2: 'two'}
print(f"type(numberDict): {type(numberDict)}")

class Foo:
    a = 0

InstanceOfFoo = Foo()
print(f"type(InstanceOfFoo): {type(InstanceOfFoo)}\n")



# Example 2: Create a type object Using type()

o1 = type('X', (object,), dict(a='Foo', b=12))

print(f"type(o1): {type(o1)}")
print(f"vars(o1): {vars(o1)}")


class test:
    a = 'Foo'
    b = 12


o2 = type('Y', (test,), dict(a='Foo', b=12))
print(f"type(o2): {type(o2)}")
print(f"vars(o2): {vars(o2)}")

"""In the program, we have used python vars() function return the __dict__ attribute. __dict__ is used
to store object's writable attributes.

You can easily change these attributes if necessary. For example, if you need to change __name__ attribute
of o1 to 'Z', simply use:"""
